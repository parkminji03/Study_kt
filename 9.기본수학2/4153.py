while True:
    l=list(map(int,input().split()))
    l.sort()
    x=l[0]
    y=l[1]
    z=l[2]
    if x==0 and y==0 and z==0:
        break
    else:
        pita=z**2
        if pita==((x**2)+(y**2)):
            print("right")
        else:
            print("wrong")