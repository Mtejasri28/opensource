x,y,z=map(int,input().split())
total= x + y
if z<x:
    print("0")
elif total>z:
    print("1")
else:
    print("2")

