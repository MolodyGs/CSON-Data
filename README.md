# Chile Social Outbreak Dataset

Interest range: November 15, 2019 – December 17, 2023

## Final Data

The final data is located in the directory: `src/archive/DATA.json`.

## Medio de Comunicación y Sesgo

| Media Outlet         | Ideology/Description                                                                   | Source                         |
| -------------------- | -------------------------------------------------------------------------------------- | ------------------------------ |
| El Mercurio          | Right-wing, Conservatism, Liberal Conservatism, Economic Liberalism                    | [Source][El Mercurio]          |
| La Cuarta            | Sensationalist, aimed at middle- and lower-class audiences                             | [Source][La Cuarta]            |
| The Clinic           | Left-wing                                                                              | [Source][The Clinic]           |
| CNN en Español       | _No clear data_                                                                        | ...                            |
| Diario Financiero    | Center-right, Liberal Conservatism, Economic Liberalism, Conservative Liberalism       | [Source][Diario Financiero]    |
| La Segunda           | Right-wing, Conservatism, Economic Liberalism, Conservative Liberalism, Anti-communism | [Source][La Segunda]           |
| La Tercera           | Moderate conservatism, Classical liberalism, Right-wing                                | [Source][La Tercera]           |
| Las Últimas Noticias | Right-wing                                                                             | [Source][Las Ultimas Noticias] |
| HoyxHoy              | Generalist                                                                             | [Source][HoyxHoy]              |
| Ciper                | Independent                                                                            | [Source][Ciper]                |
| EMOL                 | Conservatism, Right-wing                                                               | [Source][EMOL]                 |
| Ex-Ante              | _No clear data_                                                                        | ...                            |
| El Mostrador         | Pluralism                                                                              | [Source][El Mostrador]         |
| El País              | Center-left                                                                            | [Source][El Pais]              |
| Gamba                | _No clear data_                                                                        | ...                            |

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

| Media Outlet         | Data                     |
| -------------------- | ------------------------ |
| El Mercurio          | Access not allowed       |
| La Cuarta            | 153                      |
| The Clinic           | 75                       |
| CNN en Español       | 28                       |
| Diario Financiero    | SourceAccess not allowed |
| La Segunda           | SourceAccess not allowed |
| La Tercera           | 236                      |
| Las Últimas Noticias | SourceAccess not allowed |
| La Segunda           | SourceAccess not allowed |
| Ciper                | 16                       |
| EMOL                 | 153                      |
| Ex-Ante              | 65                       |
| El Mostrador         | 86                       |
| El País              | 102                      |
| Gamba                | 17                       |

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


