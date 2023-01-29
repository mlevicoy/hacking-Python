import urllib.request
import json

def main():
	ip = "181.43.201.15"
	objetivo = "https://ipinfo.io/{}/json".format(ip)  
	urlli = urllib.request.urlopen(objetivo)
	cargajson = json.loads(urlli.read())

	for dato in cargajson:
		print(dato + " : " + str(cargajson[dato]))		

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()  