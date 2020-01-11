#2012.Termino1.Evaluacion2.Tema2

def teclanum(cancion):
    tecla=[['C',1],
           ['D',3],
           ['E',5],
           ['F',6],
           ['G',8],
           ['A',10],
           ['B',12]]
    n=len(cancion)
    i=0
    secuencia=[]
    while not i>=n:
        cual=cancion[i]
        donde=-1
        j=0
        while not j>=len(tecla):
            if tecla[j][0]==cual:
                donde=j
            j=j+1
        if donde>=0:
            secuencia.append(tecla[donde][1])
        if donde<0 and cual=='#':
            k=len(secuencia)
            secuencia[k-1]=secuencia[k-1]+1
        if donde<0 and cual=='b':
            k=len(secuencia)
            secuencia[k-1]=secuencia[k-1]+1
        i=i+1
    return(secuencia)
