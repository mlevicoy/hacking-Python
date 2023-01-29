
# -*- coding: utf-8 -*-

# Importamos librería requests
import requests
# Importamos libreria bs4 y usamos el paquete BeautifulSoup
from bs4 import BeautifulSoup

# Función principal
def main():
	# Indicamos el cliente que hara la solicitud
	agente = {'User-Agent':'Firefox'}
	# Se realiza la solicitud a la página web agregando la cabecera adicional
	objetivo = requests.get(url="https://achirou.com", headers=agente)
	# Obtenemos el código en modo texto
	parseamos = BeautifulSoup(objetivo.text, 'html5lib')
	# Recorremos la variable y filtramos por la etiqueta 'link'
	for link in parseamos.find_all('link'):
		# Busca si el href contiene la ruta 'wp-content/themes/'
		if 'wp-content/themes/' in link.get('href'):
			# Obtenemos el 'href'
			tema = link.get('href')
			# Dividimos por '/'
			tema = tema.split('/')
			if 'themes' in tema:
				# Posicion de 'themes'
				posicion = tema.index('themes')
				# Extraemos el tema de WP
				temas = tema[posicion+1]
				print("El tema que se usa es: " + temas)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()

