# Medida de rendimiento: Órbitas planetarias

## Introducción

Bajo la premisa de la optimalidad del rendimiento de ***Cython*** en contraste a los tiempos de ejecución y uso de memoria dados en ***Python*** se planteó la prueba del mismo dado por un algoritmo que simula el movimiento de planetas a partir de parámetros específicos como la masa, la velocidad y la posición, dichos datos se tomaron de [aquí](https://es.wikipedia.org/wiki/Tierra). Para el desarrollo de la métrica se tomó el tiempo de ejecución por cada iteración, dentro de las cuales se hizo una variación incremental de los pasos y el marco del tiempo.

## Desarrollo

Los tiempos de ejecución que se dieron en cada una de las iteraciones fueron almacenados en el archivo *planetas.csv* los cuales incluyen las columnas de: 
* Pasos
* Marco del tiempo
* Tiempo de ejecución con las cargas en *python*
* Tiempo de ejecución con las cargas en *cython*

Con ello, se realizó un ejercicio de procesamiento y análisis de datos en el  Notebook adjunto en los ficheros.

Para hacer la reproducción satisfactoria del experimento se debe:

Clonar el repositorio

`git clone https://github.com/C-Rios/Performance-.py-.cy`make

Acceder al directorio

`cd Performance-.py-.cy`

Compilar el módulo de *cython*

`make all`

>Esto permitirá acceder a los recursos descritos en el archivo **Planeta_orbita_cy.pyx** desde *python* y *C*.

Con ello hecho es posible hacer la ejecución del archivo **main.py**, esto generará automáticamente los datos obtenidos durante la experimentación. Cabe agregar que este generará 100 iteraciones con diferentes cargas y lo almacenará en un archivo con el nombre **planeta.csv**. En el [notebook](performance_measure.ipynb) adjunto se hacen un análisis de la experimentación realizada. Si desea hacer cambios se recomienda dirigirse a las *recomendaciones* allí expuestas.



## Conclusión

A modo de conclusión se obtiene que el rendimiento dado por los tiempos de ejecución para distintas cargas en cualquiera de las aproximaciones se puede generalizar como un coste de tipo lineal como se vió en las gráficas anteriormente, con la gran diferencia de la pendiente de cada una de estas ya que en la aproximación dada por *cython* se encuentran valores de poca magnitud en relación a *python*, recordando que los tiempos de cython tiene una desviación estándar baja lo que asegura que esta medida se mantendrá dentro de los rangos esperados. Finalmente, cabe concluir que la mejora que esta dada por el uso de *cython* en contraste a *python* es simplemente colosal ya que esta tiende a mejorar el rendimiento de un programa alrededor de un *37.463 veces* en promedio, con una desviación estándar muy baja de tan solo *1.769 veces*

> Para un mayor análisis dirigirse al [notebook](performance_measure.ipynb) adjunto
