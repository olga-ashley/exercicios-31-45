Ser=int(input('Digite um número.'))
if Ser<=0:
    print('O valor não pode ser menor ou igual a 0.')
    quit()
total=float(1)
i=1
while i < Ser:
    total=total+(1/i)
    i+=1
print('A soma da série de', str(Ser), 'é',str(total)+'.')