x,y,z=map(int,input().split())
total= x + y
if total>=z:
    print("2")
elif total<z:
    print("1")
elif z<x:
    print("0")
