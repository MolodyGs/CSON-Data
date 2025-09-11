# CSON Data Collection

Rango de interés: 15 de noviembre del 2019 al 17 de Diciembre del 2023 

## Datos finales

Los datos finales se encuentra en el directorio: `src/archive/DATA.json`.

## Medios de Comunicación

### En Español

#### Medios Físicos

- El Mercurio
- La Cuarta
- The Clinic
- CNN en Español
- Diario Financiero
- La Segunda
- La Tercera
- Las Últimas Noticias
- Publimetro
- HoyxHoy

#### Medios Electrónicos

- Ciper
- EMOL
- Ex-Ante
- El Mostrador
- Ladera Sur

[Fuente de Medios](https://es.wikipedia.org/wiki/Medios_de_comunicaci%C3%B3n_en_Chile#Electr%C3%B3nicos)

### En Inglés

- AP News
- Reuters
- BBC
- CNN

### Otros

- El País

## Sesgo

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

| Medio de Comunicación | Estado                | Comentario                                                                                                                                                                                                                                                                                                                  |
| --------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| El Mercurio           | No permite el acceso  | No despliega la información, necesita de un inicio de sesión.                                                                                                                                                                                                                                                                 |
| La Cuarta             | Pendiente             | -                                                                                                                                                                                                                                                                                                                           |
| The Clinic            | Pendiente  | 403 Forbbiden. Se procede con métodos más discretos para evitar la detección.                                                                                                                                                                                                                                                                                                              |
| CNN en Español        | Pendiente              | El desglose de las noticias encontradas no son lo suficientemente extensas.                                                                                                                                                                                                                                                 |
| Diario Financiero     | No permite el acceso  | El diario financiero utiliza distintos métodos para evitar el web scraping. Inclusive evita la apertura del código fuente y no permite mostrar las opciones al hacer click derecho, entre otras técnicas. [Reddit al respecto](https://www.reddit.com/r/DataHoarder/comments/17jx5ia/how_are_we_supposed_to_counter_this/). |
| La Segunda            | No permite el acceso  | No muestra la información, requiere suscripción.                                                                                                                                                                                                                                                                            |
| La Tercera            | Datos Obtenidos!      | 269 datos.                                                                                                                                                                                                                                                                                                                   |
| Las Últimas Noticias  | Pendiente de revisión | La información desplegada en cada noticia es presentada en un formato de diario. El sitio web no permite realizar búsquedas de información. La utilización de herramientas avanzadas con google no presenta resultados favorables.                                                                                          |
| HoyxHoy               | Sitio web inestable   | El sitio web no responde efectivamente a la búsqueda de información. El sitio presenta las noticias como imágenes de diarios.                                                                                                                                                                                             |
| Ciper                 | Datos obtenidos!      | 25 datos.                                                                                                                                                                                                                                                                                                                   |
| EMOL                  | Datos obtenidos!      | 215 datos.                                                                                                                                                                                                                                                                                                                  |
| Ex-Ante               | Datos obtenidos!             | 99 datos.                                                                                                                                                                                                                                |
| El Mostrador          | Datos obtenidos!      | 99 datos.                                                                                                                                                                                                                                                                                                                   |
| El País               | En Proceso            | 128 datos.                                                                                                                                                                                                                                                                                                                   |
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
- **src → archive → pages_extracted**: Conjunto final de datos separados en carpetas según cada medio de noticias.
- **src → archive → temp**: Conjuntos de Archivos .json temporales, utilizados para pruebas sobre un conjunto de datos.
- **src → extract_code**: Conjunto de archivos .ipynb utilizados para la extracción de noticias. Cada noticiero corresponde a un archivo .ipynb individual.


