#2012.Termino2.Evaluacion3.Tema1

import random
alfabeto=[{'letra':'A','radio':'Alfa'},
            {'letra':'B','radio':'Bravo'},
            {'letra':'C','radio':'Charlie'},
            {'letra':'D','radio':'Delta'},
            {'letra':'E','radio':'Echo'},
            {'letra':'F','radio':'Foxtrot'},
            {'letra':'G','radio':'Golf'},
            {'letra':'H','radio':'Hotel'},
            {'letra':'I','radio':'India'},
            {'letra':'J','radio':'Juliet'},
            {'letra':'K','radio':'Kilo'},
            {'letra':'L','radio':'Lima'},
            {'letra':'M','radio':'Mike'},
            {'letra':'N','radio':'November'},
            {'letra':'O','radio':'Oscar'},
            {'letra':'P','radio':'Papa'},
            {'letra':'Q','radio':'Quebec'},
            {'letra':'R','radio':'Romeo'},
            {'letra':'S','radio':'Sierra'},
            {'letra':'T','radio':'Tango'},
            {'letra':'U','radio':'Uniform'},
            {'letra':'V','radio':'Victor'},
            {'letra':'W','radio':'Whiskey'},
            {'letra':'X','radio':'X-ray'},
            {'letra':'Y','radio':'Yankee'},
            {'letra':'Z','radio':'Zulu'}]
abecedario='abcdefghijklmnopq'

def coderadio(secuencia,alfabeto):
    traduccion=''
    t=len(alfabeto)
    p=len(secuencia)
    x=0
    y=0
    columna='letra'
    while not (x>=p):
        while not (y>=t):
            if (secuencia[x]==alfabeto[y][columna]):
                traduccion=traduccion+alfabeto[y]['radio']+' '
            y=y+1
        x=x+1
        y=0

    return(traduccion)

def decoradio(cadena,alfabeto):
    traduccion=''
    t=len(alfabeto)
    p=cadena.split(' ')
    q=len(p)
    x=0
    y=0
    columna='radio'
    while not (x>=q):
        while not (y>=t):
            if (p[x]==alfabeto[y][columna]):
                traduccion=traduccion+alfabeto[y]['letra']
            y=y+1
        x=x+1
        y=0

    return(traduccion)
#2012.Termino2.Evaluacion3.Tema2

cadenaal=''
fraseal=''
opcion=0
while not(opcion==4):
    print('1. Mostrar alfabeto')
    print('2. Prueba de escritura')
    print('3. Prueba de lectura')
    print('4. Salir')
    opcion=int(input('Opcion: '))
    while not (opcion>0 and opcion<=4):
        print('Ingrese opcion valida')
        opcion=int(input('Opcion: '))
    print(' ')
    if (opcion==1):
        print (alfabeto)
        print('==========================================')
    if (opcion==2):
        print('*** 2. Prueba de escritura ***')
        cadenaal=''
        fraseal=''
        x=0
        while not x>=6:
            indice=int(random.random()*(len(abecedario)))
            letra=abecedario[indice]
            cadenaal=cadenaal+letra
            x=x+1
        cadenaal=cadenaal.upper()
        print('Traduzca ', cadenaal, ' al alfabeto radiofonico')
        print('Tips: ')
        print('*Comience cada palabra con mayuscula')
        print('*Deje un espacio entre cada palabra')
        correcto=coderadio(cadenaal,alfabeto)
        intentos=1
        respuesta=input('Su respuesta: ')+' '
        while not ((intentos>=3) or (respuesta==correcto)):
                respuesta=input('Su respuesta: ')+' '
                intentos=intentos+1
        if respuesta==correcto:
            print('Respuesta correcta')
        if intentos>=3:
            print('Todos sus intentos han fallado')
        print('==========================================')
        
    if (opcion==3):
        print('*** 3. Prueba de lectura ***')
        x=0
        fraseal=''
        while not x>=6:
            indice=int(random.random()*(len(alfabeto)))
            palabra=alfabeto[indice]['radio']
            fraseal=fraseal+palabra+' '
            x=x+1
        print('Traduzca - '+fraseal+'- al alfabeto comun')
        print('Tips: ')
        print('*Todas las letras deben ser mayusculas')
        print('*No incluir espacios entre letras')
        correcto=decoradio(fraseal,alfabeto)
        intentos=1
        respuesta=input('Su respuesta: ')
        respuesta=respuesta.upper()
        while not ((intentos>=3) or (respuesta==correcto)):
                respuesta=input('Su respuesta: ')
                intentos=intentos+1
        if respuesta==correcto:
            print('Respuesta correcta')
        if intentos>=3:
            print('Todos sus intentos han fallado')
        print('==========================================')

    if (opcion==4):
        print ('Gracias por usar el software')

