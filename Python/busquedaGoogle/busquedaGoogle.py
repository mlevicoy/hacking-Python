# Permite realizar busquedas
import mechanize
# Permite colocar argumentos en la linea de comando
import argparse
# Permite extrar páginas web
from bs4 import BeautifulSoup

# Crea el objeto
argparser = argparse.ArgumentParser()
# Opciones de la línea de comando
argparser.add_argument("-b", "--buscar", help="Opción a buscar")  
# Retorna los datos
argparser = argparser.parse_args()

def main():
	# Verifica si se coloco un argumento
	if argparser.buscar:     
		# Clase navegador
		search = mechanize.Browser()
		# Si se respetan las reglas de los robots  
		search.set_handle_robots(False)	
		# Si se deben tratar los encabezados http-equiv HTML como encabezados HTTP  
		search.set_handle_equiv(False)
		# Cabecera o agente
		search.addheaders = [('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0')]
		# Definimos el buscador
		search.open("https://www.google.com")
		
		# Foco de entrada en el navegador, nr=0 nro de secuencia del formulario. 
		search.select_form(nr=0)   
		# donde q es parte de la busqueda de google
		search['q'] = argparser.buscar
		# Realiza la busqueda
		search.submit()
		# Obtiene una copia de la busqueda
		b = BeautifulSoup(search.response().read(), 'html5lib')
		for x in b.find_all('a'):
			l = x.get('href')
			l = l.replace('/url?q=', '')
			print(l)
	else:
		print("palabra que queremos buscar")

if __name__ == '__main__':
	try:
		main()     
	except KeyboardInterrupt:
		print("Saliendo")  
		exit()  