Ser=int(input('Digite um número: '))
total=1
i=1
while i <= Ser:
    fat=1
    n=i
    while n>0:
        fat=(fat*n)
        n-=1
    total=total+(1/fat)
    i+=1
print('O total da série é igual a',str(total)+'.')