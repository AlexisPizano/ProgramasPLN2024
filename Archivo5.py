import re

archivo="fime.txt"

with open(archivo,"r")as archivo:
    texto=archivo.read()

expresion_regular=re.compile(r"Est[e,a,o]")
resultado_busqueda=expresion_regular.finditer(texto)

for resultado in resultado_busqueda:
    print(resultado.group(0))