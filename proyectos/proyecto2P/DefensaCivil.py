#2006.Termino1.Evaluacion2.Tema1

opcion=0
tabla=[]
while not opcion==5:
    print('1. Registro de donacion')
    print('2. Donantes por tipo')
    print('3. Unidades por tipo')
    print('4. Guardar archivo')
    print('5. Salir')
    opcion=int(input('Opcion: '))
    while not ((opcion>=1) and (opcion<=5)):
        opcion=int(input('Opcion: '))

    if opcion==1:
        print('1. Registro de donacion')
        nombre=input('Nombre: ')
        telefono=input('Telefono: ')
        print('Tipos de donacion: Alimentos (1), Medicinas (2), Dinero (3)')
        tipodonacion=int(input('Tipo de donacion: '))
        cantidad=int(input('Cantidad: '))
        registro=[nombre,telefono,tipodonacion,cantidad]
        tabla.append(registro)
        print('*** Donacion registrada ***')
        print('======================================')
    if opcion==2:
        print('2. Donantes por tipo')
        donantes1=0
        donantes2=0
        donantes3=0
        x=0
        while not x>=len(tabla):
            if (tabla[x][2]==1):
                donantes1=donantes1+1
            if (tabla[x][2]==2):
                donantes2=donantes2+1
            if (tabla[x][2]==2):
                donantes3=donantes3+1
            x=x+1
        print('Alimentos: ',donantes1)
        print('Medicina: ',donantes2)
        print('Dinero: ',donantes3)
        print('======================================')
    if opcion==3:
        print('3. Unidades por tipo')
        unidades1=0
        unidades2=0
        unidades3=0
        x=0
        while not x>=len(tabla):
            if tabla[x][2]==1:
                unidades1=unidades1+tabla[x][3]
            if tabla[x][2]==2:
                unidades2=unidades2+tabla[x][3]
            if tabla[x][2]==3:
                unidades3=unidades3+tabla[x][3]
            x=x+1
        print('Alimentos: ',unidades1)
        print('Medicina: ',unidades2)
        print('Dinero: ',unidades3)
        print('======================================')
    if opcion==4:
        print('4. Guardar archivo')
        archivo=open('donaciones.txt','a')
        linea=0
        while not linea>=len(tabla):
            archivo.write(str(tabla[linea])+'\n')
            linea=linea+1
        archivo.close()
        print('*** Archivo guardado ***')
        print('======================================')
    if opcion==5:
        print('*** Gracias por usar el software ***')
               
