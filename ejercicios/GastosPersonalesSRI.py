#2011.Termino2.Evaluacion3.Tema3
#Anexo de gastos personales

import numpy
anexo=[]
narchivo=''
opcion=0
while not(opcion==7):
    print('1. Registra')
    print('2. Gastos por mes')
    print('3. Gastos por concepto')
    print('4. Calcula deducibles')
    print('5. Guardar archivo')
    print('6. Abrir archivo')
    print('7. Salir')
    opcion=int(input('Opcion: '))
    if (opcion==1):
        print('1. Registra factura')
        mes=int(input('Mes #:'))
        while not(mes>=1 and mes<=12):
            mes=int(input('Mes #:'))
        factura=input('Factura: ')
        ruc=input('RUC: ')
        rsocial=input('Razon Social: ')
        valor=float(input('Valor sin iva: '))
        concepto=int(input('Concepto [1-5]:'))
        while not(concepto>=1 and concepto<=5):
            print('Concepto es entre 1 y 5')
            print(' (1) Vivienda, (2) Educación, (3) Salud, (4) Vestimenta y (5) Alimentación.')
            concepto=int(input('concepto [1-5]:'))
        registro={'mes':mes, 'factura':factura, 'ruc':ruc, 'rsocial':rsocial, 'valor':valor, 'concepto':concepto}
        anexo.append(registro)
        print('***Factura registrada***')
        print('--------------------')
    
    if (opcion==2):
        print('2. Gastos por mes')
        gastosmes=numpy.zeros(shape=(13,2),dtype=float)
        for j in range(0,13,1):
            gastosmes[j,0]=j
        n=len(anexo)
        for i in range(0,n,1):
            mes=anexo[i][0]
            valor=anexo[i][4]
            gastosmes[mes,1]=gastosmes[mes,1]+valor
        print(gastosmes)
        print('--------------------')
    
    if (opcion==3):
        print('3. Gastos por concepto')
        gastostipo=numpy.zeros(shape=(6,2),dtype=float)
        for j in range(0,6,1):
            gastostipo[j,0]=j
        n=len(anexo)
        for i in range(0,n,1):
            tipo=anexo[i][5]
            valor=anexo[i][4]
            gastostipo[tipo,1]=gastostipo[tipo,1]+valor
        print(gastostipo)
        print('--------------------')
    
    if (opcion==4):
        print('4. Calcula deducibles')
        gastostipo=numpy.zeros(shape=(6,2),dtype=float)
        for j in range(0,6,1):
            gastostipo[j,0]=j
        n=len(anexo)
        for i in range(0,n,1):
            tipo=anexo[i][5]
            valor=anexo[i][4]
            gastostipo[tipo,1]=gastostipo[tipo,1]+valor
        # Ajusta a limites del SRI por monto maximo.
        total=0
        for j in range(0,6,1):
            if (gastostipo[j,1]>3000):
                gastostipo[j,1]=3000
            total=total+gastostipo[j,1]
        if (total>9000):
            total=9000
        print(gastostipo)
        print(total)
        print('--------------------')
        
    if (opcion==5):
        print('Guardar archivo')
        if (narchivo!=''):
            archivo=open(narchivo,'a')
            n=len(anexo)
            i=0
            while not i>=n:
                linea=str(anexo[i]['mes'])+','+anexo[i]['factura']+','+anexo[i]['ruc']+','+anexo[i]['rsocial']+','+str(anexo[i]['valor'])+','+str(anexo[i]['concepto'])+'\n'
                archivo.write(linea) 
                i=i+1
            archivo.close()
        else:
            narchivo='gastos.txt'
            archivo=open(narchivo,'w')
            n=len(anexo)
            i=0
            while not i>=n:
                linea=str(anexo[i]['mes'])+','+anexo[i]['factura']+','+anexo[i]['ruc']+','+anexo[i]['rsocial']+','+str(anexo[i]['valor'])+','+str(anexo[i]['concepto'])+'\n'
                archivo.write(linea) 
                i=i+1
            archivo.close()     
        print('***Archivo guardado***')
        print('--------------------')
        
    if (opcion==6):
        print('Abrir archivo')
        narchivo=input('Ingrese el nombre del archivo: ')
        anexo=[]
        print('***Archivo abierto***')
        
        
    if (opcion==7):
        print('Gracias por sus impuestos.')
