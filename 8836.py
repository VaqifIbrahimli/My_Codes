x,y=map(float, input().split())
n=(((x-y)**2)/((x**2+y**2-1)**0.5))
k=(((x**2+y**2-1)**0.5)/(2*x*y))
print(n+k)
