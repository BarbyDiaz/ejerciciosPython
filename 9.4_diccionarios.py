def encontrarPalabra(lista):
    mayor=0
    palabraMayor=" "
  

    for x in lista:
        if mayor<len(x):
            mayor=len(x)
            palabraMayor=x
    
    return palabraMayor




def f(cadena):
    dic={}
    lista=cadena.split()
    listaAux=[]


    for y in cadena:
        listaAux=[]
        for x in lista:
            if y in x:
                listaAux.append(x)
        dic[y]=encontrarPalabra(listaAux)
    return dic


texto="hola holanda humo helado victoriaaaa vicki "

dic=f(texto)

print(dic)