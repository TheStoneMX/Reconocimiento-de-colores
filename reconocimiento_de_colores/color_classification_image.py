# ----------------------------------------------
# --- Author         : Oscar Rangel
# --- Mail           : orangelca@gmail.com
# --- Date           : 16st Octuber 2017 
# ----------------------------------------------

import cv2
from helper import color_histogram_feature_extraction
from helper import knn_classifier
import os
import os.path

# read the test image
source_image = cv2.imread('black_cat.jpg')
prediction = 'n.a.'

# checking whether the training data is ready
PATH = './training.data'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print ('los datos de entrenamiento están listos, el clasificador está cargando...')
else:
    print ('se están creando datos de entrenamiento...')
    open('training.data', 'w')
    color_histogram_feature_extraction.training()
    print ('los datos de entrenamiento están listos, el clasificador se está cargando...')

# get the prediction
color_histogram_feature_extraction.color_histogram_of_test_image(source_image)
prediction = knn_classifier.main('training.data', 'test.data')
cv2.putText(
    source_image,
    'Predicción: ' + prediction,
    (15, 45),
    cv2.FONT_HERSHEY_PLAIN,
    3,
    200,
    )

# Display the resulting frame
cv2.imshow('clasificador de color', source_image)
cv2.waitKey(0)		
