#2012.Termino1.Evaluacion3.Tema3
import numpy

def colorimg(imagen):
    frecuencia=numpy.zeros(250,dtype=int)
    n,m=numpy.shape(imagen)
    i=0
    while i<=250:
        f=0
        while f<n:
            c=0
            while c<m:
                if imagen[f,c]==i:
                    frecuencia[i]=frecuencia[i]+1
                c=c+1
            f=f+1
        i=i+1
                
    return (frecuencia)
