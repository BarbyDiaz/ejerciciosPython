def crear_dic(cadena):
    dic={}




    for y in cadena:
        letra=y
        cont=0
        for x in cadena:
            if letra==x:
                cont=cont+1
                dic[letra]=cont



    return dic




cadena="hola como estas ppepepepepe"
dic=crear_dic(cadena)

print(dic)







