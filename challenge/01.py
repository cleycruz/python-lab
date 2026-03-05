#!/usr/bin/env python3

def traduccion_manual(txt_encrip):

    txt_desencrip = ""
    for l in txt_encrip:
        if 'a' <= l <= 'z':
            nuevo_codigo = (ord(l) - ord('a') + 2) % 26
            txt_desencrip  += chr(nuevo_codigo + ord('a'))
        else:
            txt_desencrip += l
    return txt_desencrip

def traduccion_avanzada(txt_encrip):
    resultado = ""
    orden_original   = "abcdefghijklmnopqrstuvwxyz"
    orden_desplazado = "cdefghijklmnopqrstuvwxyzab"
    traductor = str.maketrans(orden_original, orden_desplazado)

    resultado = txt_encrip    
    
    return resultado.translate(traductor)

# Define a main() function that prints a little greeting.

def main():
  # Get the name from the command line, using 'World' as a fallback.
    txt_encrip = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"    
    txt_desencrip = ""

    print("Forma Manual")    
    txt_desencrip = traduccion_manual(txt_encrip)
    print(txt_desencrip)   

    print("Forma Avanzada")
    txt_desencrip = traduccion_avanzada(txt_encrip)
    print(txt_desencrip)   
    
    print("Url")
    print(traduccion_manual("map"))
    print(traduccion_avanzada("map"))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
