fat=int(input('Digite um número: '))
if fat<0:
    print('Não use números negativos.')
    quit()
total=1
while fat>0:
    total=(total*fat)
    fat-=1

print('O fatorial do número indicado é igual a',str(total)+'.')