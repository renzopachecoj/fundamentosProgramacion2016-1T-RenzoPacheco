def factorial (n):
    x=1
    z=1
    while not x>n:
        z=z*x
        x=x+1
    return(z)
        
def factorialr (n):
    if n==1:
        z=1
    if n>1:
        z=n*factorialr(n-1)
    return(z)
