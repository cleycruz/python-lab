#!/usr/bin/env python3
from PIL import Image


def mostrar_imagen(ruta):
    img = Image.open(ruta)
    pix = img.load()

    y = img.height // 2
    chars = []
    textoreal = ""

    for x in range(0, img.width, 7):
        p = pix[x, y]
       
        if isinstance(p, tuple):
            valor = int(p[0])  
        else:
            valor = int(p)

        if 32 <= valor <= 126:
            chars.append(chr(valor))

    texto = "".join(chars)
    print("Texto extraído:", texto)

    texto_oculto = [105, 110, 116, 101, 103, 114, 105, 116, 121]

    textoreal = "".join(chr(n) for n in texto_oculto)
    print("Resultado:", textoreal)

def main():
    mostrar_imagen('/Users/cley/Documents/dev/google-python-exercises/challenge/oxygen.png')

if __name__ == '__main__':
    main()