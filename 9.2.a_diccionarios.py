import string

def f(cadena):
    dic={}

    lista=cadena.split()
    cant=0

    for x in lista:
        subtring=x
        cant=0

        for y in lista:
            if y==subtring:
                cant=cant+1

        dic[subtring]=cant


    return dic

cadena="hola como estas todo bien hola pepe como estas hola hola"

print(f(cadena))