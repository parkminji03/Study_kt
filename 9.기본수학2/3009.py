x=[]
y=[]

for i in range(3):
    xn,yn=map(int,input().split())
    x.append(xn)
    y.append(yn)

for i in range(3):
    if x.count(x[i])==1:
        x1=x[i]
    if y.count(y[i])==1:
        y1=y[i]
        
print(x1,y1)