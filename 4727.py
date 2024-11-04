st=input()
s=0
indeks=-1
for i in range(len(st)):
    if st[i]=='f':
        s+=1
        if s==2:
            indeks=i
            break
if indeks!=-1:
    print(indeks)
else:
    print(s-2)
