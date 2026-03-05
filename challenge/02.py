#!/usr/bin/env python3
import re 

def leer_archivo(ruta_archivo):
   with open(ruta_archivo, 'r') as f:
      archivo = f.read()
   print(archivo)
   return archivo   

def contar_caracteres(contenido):   
   match = re.findall(r"[a-z]", contenido)
   return "".join(match) 


def main():
  archivo = "/Users/cley/Documents/dev/google-python-exercises/challenge/02txt.py"
  contenido = leer_archivo(archivo)
  resultado = contar_caracteres(contenido)
  print(resultado)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()