def agenda(dicc):

    nombre=input("Porfavor, ingrese un nombre: ")
    opcion=' '
    nuevoNum=''


    while(nombre!="*"):


        if nombre in dicc:
            print("hola! "+nombre+" este es tu numero: \n", dicc[nombre])
            print("desea cambiarlo? S/N \n")
            opcion=input()

            if opcion=='S':
                nuevoNum=input("Ingrese nuevo NUMERO \n ")
                dicc[nombre]=nuevoNum
                print("Tu nuevo numero es: "+nuevoNum)

        else: 
            nuevoNum=input("Ingrese numero de telefono: \n")

            dicc[nombre]=nuevoNum


        nombre=input("Porfavor, ingrese un nombre: \n ")

        





dicc={"laura":"44554116","barby": "1524585286","erika":"11223344","damian":"77889966"}

agenda(dicc)