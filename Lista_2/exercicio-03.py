# -*- coding: utf-8 -*-
"""Exercicio-03

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nYDFduP-VHJKNYCAjGNZzghxQnBsVJLv
"""

#Para a aplicação da fórmula do NDWI: 

Xgreen = 555
Xnir = 858

NDWI = (Xnir-Xgreen)/(Xnir+Xgreen)
print("Resultado = ",NDWI)

#Para a aplicação da fórmula do NDVI

Xred = 645
Xnir = 841

NDVI = (Xnir - Xred)/(Xnir + Xred)
print ("Resultado = ", NDVI)

