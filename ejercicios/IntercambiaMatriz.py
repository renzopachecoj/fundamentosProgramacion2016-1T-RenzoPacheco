#2013.Termino2.Evaluacion3.Tema1

def intercambiar(matriz,a,b,tipo):
    n,m=numpy.shape(matriz)

    if tipo==1:
        c=0
        while not c>=m:
            t=matriz[a,c]
            matriz[a,c]=matriz[b,c]
            matriz[b,c]=t
            c=c+1

    if tipo==2:
        f=0
        while not f>=n:
            t=matriz[f,a]
            matriz[f,a]=matriz[f,b]
            matriz[f,b]=t
            f=f+1
            
    return (matriz)

def preparamatriz(matriz):
    n,m=numpy.shape(matriz)
    c=0
    mayor=0
    while not c>=(m-1):
        f=c+1
        while not (f>=n):
            if matriz[f,c]>matriz[mayor,c]:
                mayor=f
            f=f+1
        matriz=intercambiar(matriz,c,mayor,1)
        c=c+1
    
    return(matriz)

