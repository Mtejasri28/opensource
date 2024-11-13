x=int(input())
arr1=[]
for i in range(0,x):
    n=int(input())
    arr1.append(n)
for y in arr1:
    if y >= 30:
        print("YES")
    else:
        print("NO")
