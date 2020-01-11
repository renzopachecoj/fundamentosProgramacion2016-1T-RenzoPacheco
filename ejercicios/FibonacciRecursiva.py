#2007.Termino2.Evaluacion2.Tema4

def fibonaccir(i):
    if i==1:
        z=1
    if i==2:
        z=1
    if i>2:
        z=fibonaccir(i-1)+fibonaccir(i-2)
    return(z)
