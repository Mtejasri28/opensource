a,b=map(str,input().split())
a=a.upper()
b=b.upper()
if (a=='R' and b=='P'):
    print("Charan")
elif (a=='P' and b=='R'):
    print("Vignesh")
elif (a=='P' and b=='S'):
    print("Charan")
elif (a=='S' and b=='P'):
    print("Vignesh")
elif (a=='S' and b=='R'):
    print("Charan")
elif (a=='R' and b=="S"):
    print("Vignesh")
else:
    print("NULL")
