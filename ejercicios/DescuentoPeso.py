#Tarea1.Ejercicio5

precio=float(input('Cuanto cuesta: '))
peso=float(input('Cuanto pesa: '))
descuento=0

if peso>=2.01 and peso<=5:
    descuento=0.10

if peso>=5.01 and peso<=10:
    descuento=0.15

if peso>=10.01:
    descuento=0.20

pagar=peso*peso*(1-descuento)

print (pagar)
