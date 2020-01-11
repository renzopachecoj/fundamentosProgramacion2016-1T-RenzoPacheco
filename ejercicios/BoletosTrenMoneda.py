#2010.Termino1.Evaluacion1.Tema2

cantidad=float(input('Ingrese el monto de dinero: '))
moneda=float(input('Seleccione el tipo de moneda(1,2,3): '))
pasajes=float(input('Cuantos pasajes desea comprar: '))
precio=7
equivalente=cantidad

if moneda==2:
    equivalente=3.25*cantidad

if moneda==3:
    equivalente=2.50*cantidad

pagar=precio*pasajes

if equivalente>=pagar:
    cambio=equivalente-pagar
    boletos=pasajes

else:
    cambio=equivalente
    boletos=0

print (cambio)
print (boletos)

