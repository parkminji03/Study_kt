a=int(input())
for i in range(a):
    rn=[]
    h,w,n=map(int,input().split())
    for j in range(1,w+1):
        for k in range(1,h+1):
            rn.append(str(k)+str(j).zfill(2))
    print(rn[n-1])