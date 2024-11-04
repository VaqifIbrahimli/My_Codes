a, b, n=map(int, input().split())
c=a*n
d=n*b
if d>100:
    e=d//100
    c=c+e
    d=d%100
print(c,d)
