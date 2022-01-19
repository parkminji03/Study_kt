n=int(input())
newlist=[]

for i in range(666,2666800):
    if "666" in str(i):
        newlist.append(i)
        
print(newlist[n-1])