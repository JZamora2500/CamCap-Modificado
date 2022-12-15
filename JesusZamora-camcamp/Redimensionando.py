"""Redimensionar imagenes a 38x46"""
import cv2
import numpy as np
import os

# Cargamos las imagenes de la carpeta: C:\Users\JESUS ZAMORA\Desktop\Camcam\Imagenes
path = 'C:\Users\JESUS ZAMORA\Desktop\Camcam\Imagenes'
# Guardamos las imagenes en: C:\Users\JESUS ZAMORA\Desktop\Camcam\JesusZamora-camcamp\imagen\p
path2 = 'C:\Users\JESUS ZAMORA\Desktop\Camcam\JesusZamora-camcamp\imagen\p'

# Creamos una lista con los nombres de las imagenes
listaImagenes = os.listdir(path)

# Recorremos la lista de imagenes
for imagen in listaImagenes:
    # Cargamos la imagen
    img = cv2.imread(path + '/' + imagen)
    # Redimensionamos la imagen
    img = cv2.resize(img, (38, 46))
    # Renombramos a objeto_[numero].jpg y Guardamos la imagen
    cv2.imwrite (path2 + '/objeto_{}.jpg'.format(imagen), img)


    print('Imagen redimensionada: ', imagen)

print('Proceso terminado')