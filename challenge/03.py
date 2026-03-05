#!/usr/bin/env python3
import io
import re

def cargar_archivo(file_name):
    with open(file_name,'r') as f:
        archivo = f.read()
    return archivo    

def buscar_caracteres(contenido):
    match = re.findall(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', contenido)

    return match

def organizar_caracteres(lineas):
    palabra = []
    for linea in  lineas:
        caracter = linea[4]    
        print(caracter)
        palabra.append(caracter)
        #caracter += caracter
    return ''.join(palabra)

def main():
    file_name = './03.txt'
    contenido_archivo = cargar_archivo(file_name)
    print(contenido_archivo)
    lineas = buscar_caracteres(contenido_archivo)
    print(organizar_caracteres(lineas))

if __name__ == '__main__':
  main()