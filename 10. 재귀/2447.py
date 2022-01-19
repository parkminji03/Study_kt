n= int(input())
arr=[["*"]* n for _ in range(n)]

temp=n
cnt=0
while temp!= 1:
    temp/=3
    cnt+=1

for i in range(cnt):
    idx=[]
    for j in range(n):
        if (j//3**i)%3==1:
            idx.append(j)
    for k in idx:
        for r in idx:
            arr[k][r]=' '
            
print("\n".join([''.join([str(i) for i in k])for k in arr]))