# 2da Evaluación II Término 2015

import numpy

# Tema 2
def totalportipo(tabla):
    n,k =tabla.shape  # Tamaño de tabla con codigoplaya,recolectado
    
    # verifica banderas repetido cambiando a 1
    repetidos=numpy.zeros(n,dtype=int)
    i=0
    while not(i>=(n-1)):
        j=i+1
        while not(j>=n):
            if (tabla[i,0]==tabla[j,0]):
                repetidos[j]=1
            j=j+1
        i=i+1
    
    #cuenta los que se eliminan para ver los m que son únicos
    eliminar=0
    fila=0
    while not(fila>=n):
        eliminar=eliminar+repetidos[fila]
        fila=fila+1
    m=n-eliminar

    # copiar codigos unicos en tabulado columna 0
    tabulado=numpy.zeros(shape=(m,3), dtype=float)
    fila=0
    j=0
    while not(fila>=n):
        if (repetidos[fila]==0):
            tabulado[j,0]=tabla[fila,0]
            j=j+1
        fila=fila+1

    # Cuenta voluntarios por playa en tabulado columna 1
    # Acumula recolectado por playa en tabulado columna 2
    fila=0
    while not(fila>=n):
        cual=tabla[fila,0]
        # encuentra el índice en donde
        donde=numpy.where(tabulado[:,0]==cual) 
        tabulado[donde,1]=tabulado[donde,1]+1
        tabulado[donde,2]=tabulado[donde,2]+tabla[fila,1]
        fila=fila+1

    # acumula lo recolectado por playa
    return(tabulado)


# Tema 3
voluntarios=[]
opcion=0
while not(opcion==7):
    print('1. registrar voluntario')
    print('2. registrar cantidad recolectada (Kg) por voluntario')
    print('3. conteo de voluntarios')
    print('4. tabular recolectado')
    print('5. Guardar archivo')
    print('6. Abrir archivo')
    print('7. Salir')
    opcion=int(input(' opcion:'))
    
    if (opcion==1):
        print('-- registrar voluntario --')
        ced=int(input('cédula: '))
        nom=input('nombre: ')
        pla=int(input('codigo playa: '))
        rec=0
        registro={'cedula':ced,
                  'nombre': nom,
                  'playa':pla,
                  'recolectado':rec}
        voluntarios.append(registro)
        print('gracias por participar')

    if (opcion==2):
        print('-- registrar cantidad recolectada por voluntario (Kg) --')
        ced=int(input('cédula: '))
        rec=float(input('recolectado: '))
        # buscar voluntario, Podría buscar con index en la lista
        encontre=-1
        n=len(voluntarios)
        fila=0
        while not(encontre>=0 or fila>=n):
            if (voluntarios[fila]['cedula']==ced):
                encontre=fila
            fila=fila+1
        if (encontre>=0):
            voluntarios[encontre]['recolectado']=rec
            print('recolectado:',rec)
        else:
            print('no esta registrado este voluntario')

    if (opcion==3):
        print('--- cuenta voluntarios ---')
        n=len(voluntarios)
        # extraer columnas codigoplaya y recoletado
        tabla=numpy.zeros(shape=(n,2),dtype=float)
        fila=0
        while not(fila>=n):
          tabla[fila][0]=voluntarios[fila]['playa']
          tabla[fila][1]=voluntarios[fila]['recolectado']
          fila=fila+1
        resultado=totalportipo(tabla)

        print('los voluntarios presentados son:',n)
        print(resultado)

    if (opcion==4):
        print('-- tabular recolectado --')
        n=len(voluntarios)
        # extraer vector codigos playas
        tabla=numpy.zeros(shape=(n,2),dtype=float)
        fila=0
        while not(fila>=n):
          tabla[fila][0]=voluntarios[fila]['playa']
          tabla[fila][1]=voluntarios[fila]['recolectado']
          fila=fila+1
        resultado=totalportipo(tabla)

        #total recolectado
        m,k = resultado.shape
        total=0
        i=0
        while not(i>=m):
            total=total+resultado[i,2]
            i=i+1
        print('El total recolectado es:',total)
        print('El total por playa es: ')
        print(resultado)

    if (opcion==5):
        print('---- guardar el archivo de voluntarios ---')
        # prepara el modo escritura(write 'w') de archivo
        archivo=open('voluntarios.txt','w')
        n=len(voluntarios)
        fila=0
        while not(fila>=n):
            # Crea la linea de texto de los datos para un registro, separada por comas
            registro= str(voluntarios[fila]['cedula'])+','+ voluntarios[fila]['nombre'] +','+str(voluntarios[fila]['playa']) +','+str(voluntarios[fila]['recolectado']) +'\n'
            # Escribe en el archivo
            archivo.write(registro)
            fila=fila+1
        archivo.close()     # Cierra el archivo    
        print('archivo guardado...')

    if (opcion==6):
        print(' --- Abrir archivo de voluntarios---')
        voluntarios=[]
        # prepara el modo lectura(read 'r') de archivo
        archivo=open('voluntarios.txt','r')
        linea=archivo.readline()
        
        while (linea!=''):  #Hasta encontrar el final del archivo
            datos=linea.split(',')  # Divide los datos por comas
            ced=int(datos[0])
            nom=datos[1]
            pla=int(datos[2])
            rec=float(datos[3])
            # crea el registro en forma de diccionario para la lista
            registro={'cedula':ced,
                  'nombre': nom,
                  'playa':pla,
                  'recolectado':rec}
            voluntarios.append(registro)
            # Lee la siguiente linea
            linea=archivo.readline()
        archivo.close()         # Cierra el archivo    
        n=len(voluntarios)
        print(' Se recuperaron '+ str(n) + ' registros de voluntarios')
        
    if (opcion==7):
        print(' gracias por usar el software, @copyritghs')
