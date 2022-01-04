a=int(input())
b=str(input())

arr=[]
sum=0

for i in b:
    arr.append(i)

for j in range(len(arr)):
    arr[j]=int(arr[j])
    sum+=arr[j]
print(sum)