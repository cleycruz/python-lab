#!/usr/bin/env python3

import re
import requests

def consultar_pagina(url):
    pagina = requests.get(url).text     
    return pagina

def recorrer_paginas():
    urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    numero = '12345'

    for i in range(300): # Súbelo a 400 por si acaso
        url = urlbase + numero
        pagina = consultar_pagina(url)
        print(f"Paso {i}: {pagina}") # Para que sepas en qué vuelta vas
        
        # 1. Buscamos el patrón completo pero capturamos solo el número
        match = re.search(r"next nothing is (\d+)", pagina)
        
        if match:
            numero = match.group(1) # <--- IMPORTANTE: Usar el grupo 1
            
            # 2. Manejo de la trampa del 16044
            # (Aunque a veces es mejor dejar que el script pare y tú lo cambies manual,
            # así te aseguras de no saltarte pistas)
        elif "Divide by two" in pagina:
            numero = str(int(numero) // 2)
            print(f"--- Aplicando división: nuevo número {numero} ---")
        else:
           print("Fin o mensaje inesperado")
           break
    

def main():
   recorrer_paginas()


if __name__ == '__main__':
  main()