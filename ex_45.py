i=1
total=0
while i<=15:
    if i%2!=0 or i%6==0: #não sei se o +6/36 omitido na explicação é intencional
        total+=(i/i**2)
        #print(i, i**2)
    else:
        total-=(i/i**2)
        #print(-i, i**2)
    i+=1
print(total)
