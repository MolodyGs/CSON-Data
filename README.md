# Fondecyt Project - Data Collection

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

| Medio de Comunicación | Estado                | Comentario                                                          |
| --------------------- | --------------------- | ------------------------------------------------------------------- |
| El Mercurio           | No permite el acceso  | <span class="reference" data-ref="coment-el-mercurio"></span>       |
| La Cuarta             | Pendiente             | -                                                                   |
| The Clinic            | No permite el acceso  | 403 Forbbiden.                                                      |
| CNN en Español        | ¿Viable?              | <span class="reference" data-ref="coment-cnn"></span>               |
| Diario Financiero     | No permite el acceso  | <span class="reference" data-ref="coment-diario-financiero"></span> |
| La Segunda            | No permite el acceso  | <span class="reference" data-ref="coment-la-segunda"></span>        |
| La Tercera            | Datos Obtenidos!      | 23 datos.                                                           |
| Las Últimas Noticias  | Pendiente de revisión | <span class="reference" data-ref="coment-lun"></span>               |
| HoyxHoy               | Sitio web inestable   | <span class="reference" data-ref="coment-hoyxhoy"></span>           |
| Ciper                 | Datos obtenidos!      | 23 datos.                                                           |
| EMOL                  | Datos obtenidos!      | 215 datos.                                                          |
| Ex-Ante               | Pendiente             | -                                                                   |
| El Mostrador          | Pendiente             | -                                                                   |
| El País               | En Proceso            | 44 datos.                                                           |

<span class="com" id="coment-el-mercurio">No muestra la información, necesita de un inicio de sesión.</span>

<span class="com" id="coment-cnn">El desglose de las noticias encontradas no son lo suficientemente.</span>

<span class="com" id="coment-diario-financiero">El diario financiero utiliza distintos métodos para evitar el web scraping. Inclusive evita la apertura del código fuente y no permite mostrar las opciones al hacer click derecho, entre otras técnicas. <a href="https://www.reddit.com/r/DataHoarder/comments/17jx5ia/how_are_we_supposed_to_counter_this/">Reddit al respecto</a></span>.

<span class="com" id="coment-la-segunda">No muestra la información, requiere suscripción.</span>

<span class="com" id="coment-lun">La información desplegada en cada noticia es presentada en un formato de diario. El sitio web no permite realizar búsquedas de información. La utilización de herramientas avanzadas con google no presenta resultados favorables.</span>

<span class="com" id="coment-hoyxhoy">El sitio web no responde efectivamente a las búsquedas de información. El sitio presenta las noticias como imagenes de diarios.</span>

<style>
  .com{
    display: none
  }
</style>

<script>
  document.querySelectorAll('.reference').forEach(el => {
    const refId = el.getAttribute('data-ref');
    const source = document.getElementById(refId);
    if (source) el.innerText = source.innerText;
  });
</script>
