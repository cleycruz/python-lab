#!/usr/bin/env python3

import pickle

def des_serializar(banner):    
    with open(banner, 'rb') as f:
        banner_data = pickle.load(f)

    for linea in banner_data:
        #print(linea)
        for c in linea:
            print(c[0] * c[1], end="")         
        print()

def main():
    banner = 'banner.p'
    des_serializar(banner)

if __name__ == '__main__':
    main()