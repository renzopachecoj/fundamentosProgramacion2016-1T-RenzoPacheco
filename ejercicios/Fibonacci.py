#Fibonacci

n=int(input('Termino n: '))
i=2
a=1
b=1

while not (i==n):
    c=a+b
    a=b
    b=c
    i=i+1

print (c)
