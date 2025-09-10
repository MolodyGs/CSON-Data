# Chile Social Outbreak Dataset

Rango de interés: 15 de noviembre del 2019 al 17 de Diciembre del 2023 

## Datos finales

Los datos finales se encuentra en el directorio: `src/archive/DATA.json`.

## Medio de Comunicación y Sesgo

| Medio de Comunicación | Ideología/Descripción                                                                                      | Fuente                         |
| --------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------ |
| El Mercurio           | Derecha, Conservadurismo, Conservadurismo liberal, Liberalismo económico                                   | [Fuente][El Mercurio]          |
| La Cuarta             | Sensacionalista, dirigido a un público de estratos socioeconomicos medios y bajos                          | [Fuente][La Cuarta]            |
| The Clinic            | Izquierda                                                                                                  | [Fuente][The Clinic]           |
| CNN en Español        | _Sin datos claros_                                                                                         | ...                            |
| Diario Financiero     | Centroderecha, Conservadurismo liberal, Liberalismo económico, Liberalismo conservador                     | [Fuente][Diario Financiero]    |
| La Segunda            | derecha, Ideología política Conservadurismo, Liberalismo económico, Liberalismo conservador, Anticomunismo | [Fuente][La Segunda]           |
| La Tercera            | Conservadurismo moderado, liberalismo clásico, derecha                                                     | [Fuente][La Tercera]           |
| Las Últimas Noticias  | Derecha                                                                                                    | [Fuente][Las Ultimas Noticias] |
| HoyxHoy               | Generalista                                                                                                | [Fuente][HoyxHoy]              |
| Ciper                 | Independiente                                                                                              | [Fuente][Ciper]                |
| EMOL                  | Conservadurismo, derecha                                                                                   | [Fuente][EMOL]                 |
| Ex-Ante               | _Sin datos claros_                                                                                         | ...                            |
| El Mostrador          | Pluralismo                                                                                                 | [Fuente][El Mostrador]         |
| El País               | Centroizquierda                                                                                            | [Fuente][El Pais]              |
| Gamba                 | _Sin datos claros_                                                                                         | ...                            |

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

## Actividad y Resultados

| Medio de Comunicación | Datos                |
| --------------------- | -------------------- |
| El Mercurio           | No permite el acceso |
| La Cuarta             | 153                  |
| The Clinic            | 75                   |
| CNN en Español        | 28                   |
| Diario Financiero     | No permite el acceso |
| La Segunda            | No permite el acceso |
| La Tercera            | 236                  |
| Las Últimas Noticias  | No permite el acceso |
| La Segunda            | No permite el acceso |
| Ciper                 | 16                   |
| EMOL                  | 153                  |
| Ex-Ante               | 65                   |
| El Mostrador          | 86                   |
| El País               | 102                  |
| Gamba                 | 17                   |

---
## Estructura de Directorios

```
📁src/
├─ 📁archive/
│  ├─ 📁historial/
│  ├─ 📁pages_extracted/
│  ├─ 📁temp/
├─ 📁pages_extracted/
├─ 📁extract_code/
```

- **src → archive**: Corresponde a archivos .json con información extraída.
- **src → archive → historial**: Conjuntos de archivos .json historicos, esto como respaldo.
- **src → archive → pages_extracted**: Conjunto datos separados en carpetas según cada medio de noticias para su analisis.
- **src → archive → temp**: Conjuntos de Archivos .json temporales, utilizados para pruebas sobre un conjunto de datos.
- **src → extract_code**: Conjunto de archivos .ipynb utilizados para la extracción de noticias. Cada noticiero corresponde a un archivo .ipynb individual.


