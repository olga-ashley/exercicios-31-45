n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))

if n1>n2:
    print(str(n1),'é maior que', str(n2))
    i=n2
    n2=n1
    n1=i
elif n2>n1:
    print(str(n2),'é maior que', str(n1))
else:
    print('Os dois números são iguais.')
    quit()
total=0
i=n1
while i<=n2:
    if i%2!=0:
        total=total+i
    i+=1
print('O total da soma dos números ímpares entre', str(n1),'e',str(n2), 'é igual a', str(total),'.')