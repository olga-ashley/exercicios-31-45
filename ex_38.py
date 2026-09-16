arrNum=[]
total=100
i=0
while i < total:
    print('Digite o',str(i+1)+'° termo:')
    arrNum.append(int(input()))
    i+=1
high=0
low=0
i=0
while i < total:
    if high<arrNum[i]:
        high=arrNum[i]
    if low>arrNum[i]:
        low=arrNum[i]
    i+=1

print('O maior número dos que foram colocados é', str(high)+', e o menor é', str(low)+'.')