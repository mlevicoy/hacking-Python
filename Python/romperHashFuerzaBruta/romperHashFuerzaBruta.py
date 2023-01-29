# jessica : 99996b911567c83cce17cdf194f314975c57ddf1

import hashlib

def main():
	resolverhash = raw_input("Ingrese el Hash a resolver: ")
	resolver = open("resolvedordeclaves.txt", 'r')

	for x in resolver.readlines():
		a = x.strip("\n")
		a = hashlib.sha1(a).hexdigest()
		if a == resolverhash:
			print("Clave: {} El hash resuelto: {}".format(x, a))

if __name__ == '__main__':
	main()

