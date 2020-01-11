#Refuerzo Funciones

def solopares(conjunto):
    i=0
    respuesta=[]
    while i<len(conjunto):
        if conjunto[i]%2==0:
            respuesta.append(conjunto[i])
        i=i+1

    return (respuesta)
    
