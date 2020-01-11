#2015.Termino1.Evaluacion3.Tema1

def separanum(valor):

    resultado=[]

    centavos=int((valor*100)%100)
    resultado.append(centavos)

    b=int(valor)
    digito=b%10
    resultado.append(digito)

    while (b>0):
        b=int(b//10)
        if b>0:
            digito=b%10
            resultado.append(digito)
            
    return (resultado)

def cuantasmonedas(centavos):

    c50=centavos//50
    saldo=centavos-c50*50

    c25=saldo//25
    saldo=saldo%25

    c10=saldo//10
    saldo=saldo%10

    c5=saldo//5
    saldo=saldo%5

    c1=saldo

    cantidad=[c50,c25,c10,c5,c1]

    return (cantidad)

#2015.Termino1.Evaluacion3.Tema1

def deletreanumero(valor):

    separados=separanum(valor)
    deletrea=['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']

    equivale=' con '+str(separados[0])+'/100'
    equivale=deletrea[separados[1]]+equivale
    
    return (equivale)

