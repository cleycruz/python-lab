#!/usr/bin/env python3
import zipfile
import re

def leer_zip():
    archivo_zip = '06-channel.zip'
    proximo_numero = '90052'
    commentarios = []


    with zipfile.ZipFile(archivo_zip,'r') as z:
        while True:
            nombre_archivo = f'{proximo_numero}.txt'

            zipinfo = z.getinfo(nombre_archivo)
            commentarios.append(zipinfo.comment.decode('utf-8'))

            contenido = z.read(nombre_archivo).decode('utf-8')

            match = re.search(r'Next nothing is (\d+)', contenido)

            if match:
                proximo_numero = match.group(1)
            else:
                print("Final", contenido)
                break

    print("Resultado:")    
    print(''.join(commentarios))

def main():    
    leer_zip()

if __name__ == '__main__':
    main()
    