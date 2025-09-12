from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from datetime import datetime
from typing import Callable
import locale
import json
import time

months = {
    "ene": 1, "feb": 2, "mar": 3, "abr": 4,
    "may": 5, "jun": 6, "jul": 7, "ago": 8,
    "sep": 9, "oct": 10, "nov": 11, "dic": 12, "sept": 9
	}

google_classes = {
    "articles_section": "dURPMd", 
    "article": "MjjYud", 
    "date": "YrbPuc", 
    "title": "h3", 
    "description": "kb0PBd"
    }

def extract_articles_from_google(website: str, newscast: str, pages: int, output: str, keywords: str = "Estallido Social", robust: bool = True):
    if robust:
        robust_extract_articles_process(website, newscast, pages, output, keywords)
    else:
        extract_articles(website, newscast, pages, output, keywords)

# Standard extraction process without retries
def extract_articles(website: str, newscast: str, pages: int, filename: str, keywords: str = "Estallido Social", ):
	"""
    Standard extraction process without retries
    Parameters:
        website: The website to extract articles from (ex: "latercera.com")
        newscast: The name of the newscast
        pages: The number of Google pages to process
        filename: The name of the output JSON file
        keywords: The keywords to search for
	"""
	print(f"[INFO] Starting extraction process from Google...")
	
	json_pages = {"pages": []}
	filename = filename.split(".")[0]
	url = (f"https://www.google.com/search?q=%22{keywords.replace(' ', '+').lower()}%22+site%3A{website}&tbs=cdr:1,cd_min:11/15/2019,cd_max:12/17/2023&start=").strip()
 
	locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

	for page in range(0, pages):
		# Configure undetected Chrome to bypass detection
		options = uc.ChromeOptions()
		options.add_argument("--no-sandbox")
		options.add_argument("--disable-blink-features=AutomationControlled")
		driver = uc.Chrome(options=options)
		driver.set_page_load_timeout(15)
  
		try:
			# load Google search results page
			driver.get(url + str(page * 10))

			# wait for the articles section to load
			articles = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.CLASS_NAME, google_classes["articles_section"]))
			).find_elements(By.CLASS_NAME, google_classes["article"])

			# process each article
			for article in articles:
				# check if the article is from the website
				# sometimes google shows articles that are not from the website
				if (not (website in article.text)):
					continue
 
				# extract article date
				originalDate = article.find_element(By.CLASS_NAME, google_classes["date"]).find_element(By.TAG_NAME, "span").text
				day, mon_str, year = originalDate.split()
				month = months[mon_str]
				date_obj = datetime(int(year), month, int(day))
				date_epoch = int(date_obj.timestamp())

				# check if the date is between 15/11/2019 and 17/12/2023
				if (date_epoch < 1573786800 or date_epoch > 1702782000):
					continue

				# extract title, description and link
				title = article.find_element(By.TAG_NAME, "h3").text
				description = article.find_element(By.CLASS_NAME, google_classes["description"]).find_elements(By.TAG_NAME, "span")[1].text
				link = article.find_element(By.TAG_NAME, "a").get_attribute("href")

				# store article info
				link_info = {
					"newscast": newscast,
					"title": title,
					"description": description,
					"category": "Not found initially",
					"date": originalDate,
					"image_link": "Not found initially",
					"author": "Not found initially",
					"link": link,
                    "content": "The content has not been extracted yet"
				}
				json_pages["pages"].append(link_info)
    
		except:
			print("[ERROR] An error occurred while processing search result. Page index:", page)
   
		finally:
			# Ensure the driver is closed properly
			driver.quit()

	# Save the extracted information
	print(f"\n[INFO] Storing information in JSON file at [{filename}.json]")
	with open(f"{filename}.json", "w", encoding="utf-8") as file:
		json.dump(json_pages, file, ensure_ascii=False, indent=4)

def extract_data_from_page(
    get_author: Callable[[WebElement], str],
    get_description: Callable[[WebElement], str],
    get_content: Callable[[WebElement], str],
    input_file, output_file,
    before_func: Callable[[], any] = None,
    limit_of_pages: int = 1,
    wait=20):

	extracted_pages = {"pages": []}
	extracted_pages_with_content = {"pages": []}

	print(f"[INFO] Input file: {input_file}")
	print(f"[INFO] Output file: {output_file}")
	print(f"[INFO] Limit of pages to process: {limit_of_pages}")

    # Load the extracted pages from the input JSON file
	print("\n[INFO] Loading extracted pages from JSON file...")
	with open(input_file, 'r', encoding='utf-8') as file:
		extracted_pages = json.load(file)

	# Extract data from each page
	print("[INFO] Starting extraction process...")
	for page_index, page in enumerate(extracted_pages["pages"]):

		# Check if the limit of pages to process has been reached
		if page_index >= limit_of_pages:
			print("[INFO] Limit of pages reached.")
			break

		# Process the page
		print(f"\n[INFO] Checking page: {page_index} | Link: {page['link']}" )
		try: 
			options = uc.ChromeOptions()
			options.add_argument("--no-sandbox")
			options.add_argument("--disable-blink-features=AutomationControlled")
			driver = uc.Chrome(options=options)
			driver.set_page_load_timeout(wait)
			driver.get(page['link'])
			driver = before_func(driver) if before_func is not None else driver
			body=WebDriverWait(driver, wait).until(
				EC.presence_of_element_located((By.TAG_NAME, 'body'))
			)

			# Extract author, description and content using the provided functions
			author = get_author(body)
			description = get_description(body)
			content = get_content(body)

			# Store the extracted information
			page["content"] = content
			page["author"] = author
			page["description"] = description
			extracted_pages_with_content["pages"].append(page)


		except Exception as e:
			print(f"[ERROR] An error occurred while processing page {page_index}: {e}")
			page["content"] = "[ERROR] Content could not be extracted due to an error"
			page["author"] = "[ERROR] Author could not be extracted due to an error"
			page["description"] = "[ERROR] Description could not be extracted due to an error"
			extracted_pages_with_content["pages"].append(page)

		finally:
			# Close the driver
			driver.quit()
    
			# Save the extracted information to the output JSON file after each page
			print("[INFO] Storing information in a JSON file...")
			with open(output_file, 'w', encoding='utf-8') as file:
				json.dump(extracted_pages_with_content, file, ensure_ascii=False, indent=4)

def robust_extract_articles_process(website: str, newscast: str, pages: int, output: str, keywords: str = "Estallido Social"):
	print("[INFO] Starting extraction process from Google...")
	print("[INFO] Website:", website)
	print("[INFO] Newscast:", newscast)
	print("[INFO] Pages to extract:", pages)
	print("[INFO] Keywords:", keywords)

	json_pages = {"pages": []}
	output = output.split(".")[0]
	keywords = keywords.replace(" ", "+").lower()
	url = f"https://www.google.com/search?q=%22{keywords}%22+site%3A{website}&tbs=cdr:1,cd_min:11/15/2019,cd_max:12/17/2023&start="

	articles_successfully_extracted = 0
	articles_failed_extraction = 0
	pages_succeeded = 0
	pages_failed = 0
	page_fatal_error = False

	if output == "":
		print("[ERROR] Output filename cannot be empty.")
		return 

	locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
	for page in range(0, pages):
		print(f"[INFO] Checking Google page | Page Index: {page}")
		try: 
			options = uc.ChromeOptions()
			options.add_argument("--no-sandbox")
			options.add_argument("--disable-blink-features=AutomationControlled")
			driver = uc.Chrome(options=options)
			url = (f"https://www.google.com/search?q=%22{keywords.replace(' ', '+').lower()}%22+site%3A{website}&tbs=cdr:1,cd_min:11/15/2019,cd_max:12/17/2023&start={page * 10}").strip()
			print(f"\n[INFO] Google URL: {url}")
			driver.get(url)

			articles_section = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.CLASS_NAME, "dURPMd"))
			)
			articles = articles_section.find_elements(By.CLASS_NAME, "MjjYud")

			print(f"[INFO] {len(articles)} articles found")
			for i, article in enumerate(articles):
				max_retries = 3
				for attempt in range (0, max_retries):
					print(f"\n[INFO] Checking article... | Article Index {i}")
					try: 
						# check if the article is from the website
						# sometimes google shows articles that are not from the website
						if (not (website in article.text)):
							print(f"[INFO] The article is not from {website}. Skipping...")
							break

						# extract article date
						originalDate = article.find_element(By.CLASS_NAME, "YrbPuc").find_element(By.TAG_NAME, "span").text
						day, mon_str, year = originalDate.split()
						month = months[mon_str]
						date_obj = datetime(int(year), month, int(day))
						date_epoch = int(date_obj.timestamp())
	
						# check if the date is between 15/11/2019 and 17/12/2023
						if (date_epoch < 1573786800 or date_epoch > 1702782000):
							print(f"[INFO] The article date is out of range (15/11/2019 - 17/12/2023). Skipping...")
							break

						# extract title, description and link
						print(f"[INFO] Extracting title, description and link...")
						title = article.find_element(By.TAG_NAME, "h3").text
						description = article.find_element(By.CLASS_NAME, "kb0PBd").find_elements(By.TAG_NAME, "span")[1].text 
						link = article.find_element(By.TAG_NAME, "a").get_attribute("href")
						description = description if description != "" else "not found initially"
						print(f"[INFO] Article information extracted successfully!")

						# store article info
						link_info = {
							"newscast": newscast,
							"title": title,
							"description": description,
							"category": "not found initially",
							"date": originalDate,
							"image_link": "not found initially",
							"author": "not found initially",
							"link": link,
						}

						json_pages["pages"].append(link_info)
						articles_successfully_extracted += 1
						break

					except Exception as e:
						print(f"[ERROR] A error occurred while processing search result. Page index: {page}")
						print(f"[ERROR] Google result URL: {url}")
						print(f"[ERROR] Error message: {e}")

						# Retry logic
						if attempt < max_retries - 1:
							time.sleep(2)
							print(f"[INFO] Retrying... (Attempt {attempt + 1} of {max_retries})")
							continue
						else:
							print(f"[ERROR] A error occurred while extracting data from a article. Skipping article.")
							print(f"[ERROR] Error message: {e}")
							articles_failed_extraction += 1
							break
   
		except Exception as e:
			print(f"[ERROR] A fatal error occurred while processing search result. Page index: {page}")
			print(f"[ERROR] Google result URL: {url}")
			print(f"[ERROR] Error message: {e}")
			page_fatal_error = True
			continue

		finally:
			if page_fatal_error:
				page_fatal_error = False
				pages_failed += 1
			else:   
				pages_succeeded += 1
			driver.quit()


	# Save the extracted information
	print(f"\n[INFO] Storing information in JSON file at [{output}.json]")
	with open(f"{output}.json", "w", encoding="utf-8") as file:
		json.dump(json_pages, file, ensure_ascii=False, indent=4)
						
	# ----------------- Stats -----------------
	print("\n\n")
	print("----- STATS -----")

	try:
		print(f"Amount of pages processed: {pages}")
		print(f"% Pages succeeded [{pages_succeeded}]: {round(100 * pages_succeeded/pages, 2)}")
		print(f"% Pages failed [{pages_failed}]: {round(100 * pages_failed/pages, 2)}")
		print(f"% Articles succeeded [{articles_successfully_extracted}]: {round(100 * articles_successfully_extracted/(articles_successfully_extracted + articles_failed_extraction), 2)}")
		print(f"% Articles failed [{articles_failed_extraction}]: {round(100 * articles_failed_extraction/(articles_successfully_extracted + articles_failed_extraction), 2)}")

	except: 
		print("A error occurred while processing the stats")

