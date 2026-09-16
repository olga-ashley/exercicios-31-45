i=1
total=0
while i <=50:
    res=i/((i*2)-1)
    #print(i, (i*2)-1)
    total=total+res
    i+=1
print('A somatória da série é igual a', str(total)+'.')