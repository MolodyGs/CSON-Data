# Chile Social Outbreak Dataset

Interest range: November 15, 2019 – December 17, 2023

## Final Data

The final data is located in the directory: `src/archive/DATA.json`.

## Medio de Comunicación y Sesgo

| Media Outlet         | Ideology/Description                                                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| El Mercurio          | Right-wing politics. Conservative-liberal vision, mainly aimed at business sectors, politicians, and Chilean elites.                                         |
| La Cuarta            | Right-wing politics. Popular and sensationalist focus, mainly aimed at workers, middle, and lower classes.                                                   |
| The Clinic           | Left-wing politics. Progressive-critical line, oriented towards young people, university students, and urban sectors with an alternative political outlook.  |
| CNN en Español       | Liberal-centrist editorial line, aimed at a Latin American audience interested in politics, economy, and current affairs.                                    | ... |
| Diario Financiero    | Pro-market liberal vision, oriented towards businesspeople, executives, investors, and economic decision-makers.                                             |
| La Segunda           | Right-wing politics. Conservative-liberal line, focused on professionals, politicians, and businesspeople.                                                   |
| La Tercera           | Right-wing politics. Liberal-centrist line, aimed at middle classes, professionals, academics, and readers of national politics.                             |
| Las Últimas Noticias | Right-wing politics. Entertainment and apolitical focus, aimed at a mass, young, and digital consumer audience.                                              |
| HoyxHoy              | Right-wing politics. Citizen and neutral focus, oriented towards an urban, young audience and public transport users.                                        |
| Ciper                | Independent. Critical line, aimed at those interested in investigative journalism, transparency, and Chilean politics.                                       |
| EMOL                 | Right-wing politics. Centrist-liberal editorial line, aimed at a general audience, professionals, academics, and readers of national and international news. |
| Ex-Ante              | Center-right politics. Analytical and critical focus, directed at politicians, professionals, businesspeople, and readers of national political affairs.     | ... |
| El Mostrador         | Pluralist. Progressive and independent line, directed at urban readers, young people, academics, and politically engaged Chileans.                           |
| El País              | Center-left politics. Progressive and critical focus, aimed at an international audience and readers interested in global politics.                          |
| Gamba                | _No clear data_                                                                                                                                              | ... |

[El Mostrador]: https://es.wikipedia.org/wiki/El_Mostrador
[La Cuarta]: https://es.wikipedia.org/wiki/La_Cuarta
[The Clinic]: https://es.wikipedia.org/wiki/The_Clinic
[Diario Financiero]: https://es.wikipedia.org/wiki/Diario_Financiero
[La Segunda]: https://es.wikipedia.org/wiki/La_Segunda
[La Tercera]: https://es.wikipedia.org/wiki/La_Tercera
[Las Ultimas Noticias]: https://es.wikipedia.org/wiki/Las_%C3%9Altimas_Noticias
[HoyxHoy]: https://es.wikipedia.org/wiki/HoyxHoy
[Ciper]: https://es.wikipedia.org/wiki/Ciper
[EMOL]: https://es.wikipedia.org/wiki/EMOL
[El Mercurio]: https://es.wikipedia.org/wiki/El_Mercurio
[El Pais]: https://es.wikipedia.org/wiki/El_Pa%C3%ADs

## Activity and Results

| Media Outlet         | Data               |
| -------------------- | ------------------ |
| El Mercurio          | Access not allowed |
| La Cuarta            | 153                |
| The Clinic           | 75                 |
| CNN en Español       | 28                 |
| Diario Financiero    | Access not allowed |
| La Segunda           | Access not allowed |
| La Tercera           | 236                |
| Las Últimas Noticias | Access not allowed |
| La Segunda           | Access not allowed |
| Ciper                | 16                 |
| EMOL                 | 153                |
| Ex-Ante              | 65                 |
| El Mostrador         | 86                 |
| El País              | 102                |
| Gamba                | 17                 |

## Directory Structure

```
📁src/
├─ 📁archive/
│  ├─ 📁historial/
│  ├─ 📁pages_extracted/
│  ├─ 📁temp/
├─ 📁pages_extracted/
├─ 📁extract_code/
```

- **src → archive**: Contains .json files with extracted information.
- **src → archive → historial**: Sets of historical .json files kept as backup.
- **src → archive → pages_extracted**: Dataset divided into folders by news outlet for analysis.
- **src → archive → temp**: Temporary .json files used for testing on subsets of data.
- **src → extract_code**: Collection of .ipynb files used for news extraction. Each outlet corresponds to an individual notebook.


