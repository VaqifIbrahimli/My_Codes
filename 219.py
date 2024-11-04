h,w,l,k=map(int, input().split())
V=h*l*w
if V%k!=0:
    print((V//k)+1)
else:
    print(V//k)
