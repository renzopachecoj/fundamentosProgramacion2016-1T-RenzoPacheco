#2012.Termino1.Evaluacion1.Tema4

consumo=float(input('Ingrese el consumo electrico: '))
estacion=int(input('Ingrese la estacion (1=invierno 2=verano): '))

if estacion==1:
    tarifa=0.04
    if consumo>=130 and consumo<500:
        tarifa=0.11
    if consumo>=500 and consumo<700:
        tarifa=0.13
    if consumo>=700:
        tarifa=0.26
    
if estacion==2:
    tarifa=0.04
    if consumo>=130 and consumo<500:
        tarifa=0.08
    if consumo>=500 and consumo<700:
        tarifa=0.11
    if consumo>=700:
        tarifa=0.16

valor=tarifa*consumo

print ('Valor de la factura: ' , valor)
