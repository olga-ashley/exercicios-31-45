numA=int(input('Insira o primeiro número: '))
numB=int(input('Insira o segundo número: '))
if numB<=0 or numA<=0:
    print('Use números maiores ou iguais a 1.')
    quit()
if numA>numB:
    i=numA
    numA=numB
    numB=i
j=numA
print('Os números primos entre',numA,'e',numB,'são:') 
while j <= numB:
    primo=True
    i=2
    while i < j:
        if j%i==0: #se j é multiplo de i
            primo=False
        i+=1
    if primo==True:
        print(j)
    j+=1
