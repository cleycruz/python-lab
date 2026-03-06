#!/usr/bin/env python3
import bz2

def descifrar():
    us = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    dus = bz2.decompress(us).decode()
    dpw = bz2.decompress(pw).decode()

    print(f'u: {dus}    p: {dpw} ')

def main():
    descifrar()

if __name__ == '__main__':
    main()