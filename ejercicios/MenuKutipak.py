#2015.Termino1.Evaluacion2.Tema2

def kutipak(palabra, modo, diccionario):
    
    resultado=''
    t=len(diccionario)
    donde=-1
    fila=0
    
    if (modo==1): # Busca quichua a español
        columna='quichua'
        while not(fila>=t or donde>=0):
            if (palabra==diccionario[fila][columna]):
                donde=fila
                resultado=diccionario[donde]['espanol']
            fila=fila+1

    if (modo==2):   # Busca español a quichua
        columna='espanol'
        while not(fila>=t or donde>=0):
            if (palabra==diccionario[fila][columna]):
                donde=fila
                resultado=diccionario[donde]['quichua']
            fila=fila+1

    return(resultado)

# Tema 2. Manejo del menu
diccionario=[ {'quichua':'man','espanol':'al'},
              {'quichua':'wasi','espanol':'casa'},
              {'quichua':'pak', 'espanol':'del'},
              {'quichua':'kuska', 'espanol':'lugar'}]

# Menu
opcion=1
while not(opcion==6):
    print('1. Traducir palabras')
    print('2. Traducir una frase')
    print('3. Añadir palabras al diccionario')
    print('4. Guardar archivo del diccionario')
    print('5. Abrir archivo del diccionario')
    print('6. Salir')
    opcion=int(input('Cual opcion: '))
    
    if (opcion==1):
        print('--- Traducir palabras ---')
        palabra=input('Palabra: ')
        modo=int(input('Modo (1)q-e (2)e-q:'))
        traducido=kutipak(palabra,modo,diccionario)
        print(traducido)

    if (opcion==2):
        print('--- Traducir una frase ---')
        frase=input('Frase: ')
        modo=int(input('modo (1)q-e (2)e-q:'))
        palabra=frase.split(' ')
        t=len(palabra)
        traducido=''
        i=0
        while not i>=t:
            otra=kutipak(palabra[i],modo,diccionario)
            if (otra==''):
                otra=palabra[i]
            traducido=traducido + ' ' + otra
            i=i+1
        print(traducido)
        
    if (opcion==3):
        print('--- Añadir palabras al diccionario ---')
        traduccion=[]
        pquichua=input('Palabra en quichua: ')
        pespanol=input('Palabra en español: ')
        traduccion={'quichua':pquichua,'espanol':pespanol}
        diccionario.append(traduccion)
        print('Nueva traduccion añadida: ')
        print(traduccion)
               
    if (opcion==4):
        print('--- Guardar archivo del diccionario ---')  
    if (opcion==5):
        print('--- Abrir archivo del diccionario ---')
    if (opcion==6):
        print('--- Gracias por usar el software ---')
