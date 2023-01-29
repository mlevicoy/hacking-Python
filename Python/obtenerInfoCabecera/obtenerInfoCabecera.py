# -*- coding: utf-8 -*-
#python obtenerInforCabecera.py -t <http://pagina.cl>

import requests
# permite pesar parámetros fuera de la hoja de código
import argparse

# Crea el objeto
parser = argparse.ArgumentParser()
# Se especifica las opciones de línea de comando
parser.add_argument('-t', '--target', help='Objetivo')
# Retorna los datos de las opciones especificadas
parser = parser.parse_args()

def main():
	# Si existe el objetivo
	if parser.target:
		try:
			objetivo = requests.get(url=parser.target)    
			header = dict(objetivo.headers)
			for x in header:
				print(x + " : " + header[x])
		except:
			print("No me puedo conectar")
	else:
		print("Escribe bien el objetivo")

if __name__ == '__main__':
  	main()  
