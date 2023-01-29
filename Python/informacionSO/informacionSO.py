from subprocess import check_output
import subprocess

sistema = check_output('systeminfo', stderr=subprocess.STDOUT)

registro = open('registro.txt', 'wb')
registro.write(sistema)
print("Confirmación de información sustraida")
registro.close()




