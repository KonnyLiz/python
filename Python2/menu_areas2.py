#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importar el script de areas
import areas2 as areas
if __name__ == "__main__":  
	respuesta=True
	while respuesta:
		print ("""
		1. Calcular el area de un triángulo
		2. Calcular el area de un rectángulo
		3. Calcular el área del circulo
		4. Salir
		""")
		respuesta=raw_input("Seleccione una ópcion: ") 
		if respuesta=="1": 
			print("\n Calculo del área de un triangulo") 
			areatriangulo=areas.Triangulo()
			areatriangulo.cargar_base()
			areatriangulo.cargar_altura()
			areatriangulo.calcular()
		elif respuesta=="2":
			print("\n Calculo del área de un rectánculo") 
			arearectangulo=areas.Rectangulo()
			arearectangulo.cargar_base()
			arearectangulo.cargar_altura()
			arearectangulo.calcular()
		elif respuesta=="3":
			print("\n Calculo del área de un círculo") 
			#r=float(raw_input("Radio: "))
			areacirculo=areas.Circulo()
			areacirculo.cargar_radio()
			areacirculo.calcular()
		elif respuesta=="4":
			print("\n Adios!") 
			respuesta = False
		else:
			print("\n No es una opción valida, pruebe de nuevo")
			respuesta = True
