# -*- coding: utf-8 -*-

# Permite trabajar con DNS
# python3 -m pip install dnspython
import dns.resolver

def main():
	try:
		# Aqui van los Query Code
		objetivo = dns.resolver.resolve("achirou.com", "NS")
		for x in objetivo:
			print(x)
	except:
		print("No pude obtener información.")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()