n=int(input('Digite um número: '))
i=0
arrFib=[1,1]
while i<n:
    if i>1:
        arrFib.append(int(arrFib[i-1]+arrFib[i-2]))
    print(arrFib[i])
    i+=1