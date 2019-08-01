# Reconocimiento-de-colores
El reconocimiento de color tanto en una transmisión de cámara web en tiempo real, en video y en una sola imagen usando el algoritmo de clasificación de aprendizaje automático de vecinos más cercanos de K está entrenado con características de histograma de color.
Este proyecto se centra en la clasificación del color por el clasificador de aprendizaje automático K-Nearest Neighbours, que está capacitado por el histograma de color R, G, B. Puede clasificar Blanco, Negro, Rojo, Verde, Azul, Naranja, Amarillo y Violeta. Si desea clasificar más color o mejorar la precisión, debe trabajar en los datos de entrenamiento o considerar otras características de color, como Momentos de color o Correlograma de color .

Puede usar color_recognition_api para realizar el reconocimiento de color en tiempo real en sus proyectos. Puede encontrar un ejemplo de uso de color_recognition_api en este repositorio .

¿Qué hace este programa?

Extracción de características: realice la extracción de características para obtener los valores de histograma de color R, G, B de las imágenes de entrenamiento
Clasificador de Vecinos K-Nearest de entrenamiento: Clasificador de KNN de entrenamiento por valores de histograma de color R, G, B
Clasificación por KNN entrenado: lea la cámara web cuadro por cuadro, realice la extracción de características en cada cuadro y luego clasifique el color medio por clasificador KNN entrenado.

TODOS:

Se agregará la utilidad "Agregar nuevo color".
Se agregarán nuevos extractores de funciones.
Se agregarán nuevos clasificadores.
Teoría
En este estudio, los colores se clasifican utilizando el algoritmo clasificador de aprendizaje automático K-Neares Neşghbor. Este clasificador está entrenado por los valores del histograma de color R, G, B de la imagen. El flujo de trabajo general se da a continuación.

Imagen

Debe conocer 2 fenómenos principales para comprender los sistemas básicos de detección / reconocimiento de objetos de la visión artificial y el aprendizaje automático.

**1.) Feature Extraction**

Cómo representar los puntos interesantes que encontramos para compararlos con otros puntos interesantes (características) en la imagen.

2.) Clasificación

Un algoritmo que implementa la clasificación, especialmente en una implementación concreta, se conoce como clasificador. El término "clasificador" a veces también se refiere a la función matemática, implementada por un algoritmo de clasificación, que asigna datos de entrada a una categoría.

Para este proyecto;

1.) Extracción de características = Histograma de color

Color Histogram es una representación de la distribución de colores en una imagen. Para las imágenes digitales, un histograma de color representa el número de píxeles que tienen colores en cada una de una lista fija de rangos de color, que abarcan el espacio de color de la imagen, el conjunto de todos los colores posibles.

imagen 

2.) Clasificación = K-Algoritmo de vecinos más cercanos

K vecinos más cercanos es un algoritmo simple que almacena todos los casos disponibles y clasifica los nuevos casos en función de una medida de similitud (por ejemplo, funciones de distancia). KNN se ha utilizado en la estimación estadística y el reconocimiento de patrones ya a principios de la década de 1970 como una técnica no paramétrica.

Implementación
OpenCV se usó para cálculos de histograma de color y clasificador knn. Se usó NumPy para los cálculos de matriz / matriz n-dimensional. El programa fue desarrollado en Python en un entorno Linux.

En la carpeta " src ", hay 2 clases de Python que son:

color_classification_webcam.py : clase de prueba para realizar reconocimiento de color en tiempo real desde la transmisión de la cámara web.

color_classification_image.py : clase de prueba para realizar reconocimiento de color en una sola imagen.

En la carpeta " color_recognition_api ", hay 2 clases de Python que son:

feature_extraction.py : clase de operación de extracción de características

knn_classifier.py : clase de clasificación knn

1.) Explicación de " feature_extraction.py "

Puedo obtener el histograma de imágenes en color RGB de esta clase de Python. Por ejemplo, la gráfica del histograma de color RGB para una de las imágenes rojas se muestra a continuación.

imagen

Decidí usar el número bin del histograma que tiene el valor máximo del recuento de píxeles para R, G y B como característica para poder obtener los valores dominantes R, G y B para crear vectores de características para el entrenamiento. Por ejemplo, los valores dominantes R, G y B de la imagen roja que se da arriba son [254, 0, 2].

Obtengo los valores dominantes de R, G, B usando Histograma de color para cada imagen de entrenamiento y luego los etiqueto porque el clasificador KNN es un alumno supervisado y despliegue estos vectores de características en el archivo csv. Por lo tanto, creo mi conjunto de datos de vectores de características de entrenamiento. Se puede encontrar en el archivo cuyo nombre es training.data en la carpeta src.

2.) Explicación de " knn_classifier.py "

Esta clase proporciona estos cálculos principales;

Obteniendo datos de entrenamiento
Obteniendo características de imagen de prueba
Cálculo de la distancia euclidiana
Conseguir k vecinos más cercanos
Predicción de color
Devolver la predicción es verdadero o falso
" Color_classification_webcam.py " es la clase principal de mi programa, proporciona;

Llamar a feature_extraction.py para crear datos de entrenamiento mediante extracción de características
Llamar a knn_classifier.py para la clasificación
Puede encontrar datos de entrenamiento aquí .

Puede encontrar características obtenidas de los datos de entrenamiento aquí .

Conclusión
Creo que los datos de entrenamiento tienen una gran importancia en la precisión de la clasificación. Creé mis datos de entrenamiento con cuidado, pero tal vez la precisión puede ser mayor con datos de entrenamiento más adecuados.

Otra cosa importante son los rayos y las sombras. En mis imágenes de prueba, las imágenes que se tomaron en condiciones de poca luz y con sombras se clasifican incorrectamente (falsos positivos), tal vez algún algoritmo de filtrado debería / pueda implementarse antes de que las imágenes de prueba se envíen al clasificador KNN. Por lo tanto, se puede mejorar la precisión.

Citación
Si usa este código para sus publicaciones, cítelo como:

@ONLINE{cr,
    author = "Oscar Rangel",
    title  = "Color Recognition",
    year   = "2018",
    url    = "https://github.com/TheStoneMX/Reconocimiento-de-colores/"
}
