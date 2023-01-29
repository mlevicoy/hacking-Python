# -*- coding: utf-8 -*-

# Importamos librería requests
import requests
# Importamos librería para trabajar con ficheros
from os import path
# Importamos librería para barra de progresos 
from progress.bar import Bar

def main():
	# Verificamos si existe el fichero
	if path.exists("wp_plugins.txt"):
		# Agregamos el contenido en la variable
		plugins = open("wp_plugins.txt", "r")
		# Separamos por salto de línea
		plugins = plugins.read().split('\n')
		lista = []
		objetivo = "http://cibseg.cl/monumentopatagonia"
		barra = Bar("Procesando...", max=len(plugins))
		# Recorremos el contenido
		for plugin in plugins:
			barra.next()
			try:
				# Sacamos la información de la WEB
				plu = requests.get(url=objetivo+"/"+plugin)
				if plu.status_code == 200:
					resultado = objetivo+""+plugin
					lista.append(resultado.split("")[-2])
			except:
				pass
		barra.finish()
		for plugin in lista:
			print("Plugins: {}".format(plugin))
	else:
		print("No se encontro la lista")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()