#2007.Termino1.Evaluacion2.Tema1

def par(n):
    if n==0:
        z=1
    if n>0:
        z=impar(n-1)
    return(z)
def impar(n):
    if n==0:
        z=0
    if n>0:
        z=par(n-1)
    return(z)
