#!/usr/bin/python3

def repeat(s, exclamacion):
    """Retrorna el cadenas s , pero repetiendola tres veces
    si la  exclamacion es True sse agrega este simbolo"""

    result = s * 3
    if exclamacion:
        result = result + "!"    
    return result
    
def cadenas():
    cadena = "Esta es una cadena"
    print(cadena[len(cadena)-1])
    print(len(cadena))
    return cadena

def cadenas2():
    address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
    {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
    {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

    for person  in address_book:
        print(f'Nombre: {person["name"]:6}  Dirección: {person["addr"]:10}')

def main():
    # print(repeat("Mi Juliachy ", True))
    # print(repeat("testing ", False))
    # cadenas()∫
    # raw = r'this    \t\n and that'

    # this\t\n and that
        # print(raw)

    # multi = """It was the best of times.
    #  It was the worst of times."""

    # It was the best of times.
    #   It was the worst of times.        
    # print(multi)
    cadenas2()

if __name__ == '__main__':
    main()
