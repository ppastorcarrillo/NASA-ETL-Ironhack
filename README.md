# NASA-ETL-Ironhack
***
![](images/NASA_logo.svg.png)
***
Este es mi primer proyecto ETL en Ironhack.
El proyecto consta de varias partes.
***


# Extracción

### CSV principal:

La primera era obtener un csv de la pagina www.kaggle.com, que tubiera menos de un 6 de usabilidad.
Yo he elegido un csv de exoplanetas de la NASA, en la cual aparecen los exoplanetas confirmados en su presencia.
El csv que elegi es este:
![csv kaggle](https://www.kaggle.com/datasets/harmanjotsingh12js/nasa-exoplanets-exploration-data)

Este venia bastante bien ordenado y con varios valores nulos. 
Esta seria la tabla:
![principal](csv/nasa_exoplanets.csv)

### Tabla complementaria:

Encontre un tabla complementaria que tenia un dato curioso, que es el indice de impacto del exoplaneta.

![](images/colision.jfif)

En mi entender a menor indice de impacto, con un rango de 0 a 1, a mayor indice mas perpendicular va a colisionar con el otro objeto y menor posibilidad de rebotar.

Esta es la definicion en google: 
"En física, el parámetro de impacto b se define como la distancia perpendicular entre la trayectoria de un proyectil y el centro de un campo potencial U(r) creado por un objeto al que se acerca el proyectil."

La tabla es:
![complementaria](csv/cumulative_2023.01.11_04.18.35.csv)
### Escrapeo

Queria escrapear la imagen asociada a los exoplanetas pero por problemas técnicos solo me quede con una descripción y año de descubriento del exoplaneta.

![Exoplanetas](https://exoplanets.nasa.gov/exep/search.html?q=)

Este escrapeo se puede ver en este csv:
![escrapeo](csv/scraping.csv)

# Limpieza
 
La limpieza no fue muy complicada y el resultado lo tendria estaria en este csv:
![final](csv/definitivo.csv)





# Analisis y Visualización 





