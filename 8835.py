x,y=map(float, input().split())
n=(((x**2+y**2)**0.5)/((x-y)**2))-((2*x*y)/((x**2+y**2)**0.5))
print(n)
