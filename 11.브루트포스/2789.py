n,m=map(int,input().split())
a=list(map(int,input().split()))
a=a[0:n+1]
b=[]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for k in range(n):
            if i==k or j==k:
                continue
            else:
                if a[i]+a[j]+a[k]<=m:
                    b.append(a[i]+a[j]+a[k])

print(max(b))