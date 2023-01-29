import os

# Ubicación del archivo que se esta ejecutando
print("Ubicacion archivo Python: " + os.getcwd())
# Establece una ubicación
os.chdir("C:/Users/Manuel Levicoy O/OneDrive - Bogado Ingenieros Consultores SpA/Udemy - Hacking Python 3/Python")
# Ubicación actual
print("Ubicacion actual: " + os.getcwd())
# Lista ficheros y directorios en la ubicación actual
print(os.listdir(os.getcwd()))