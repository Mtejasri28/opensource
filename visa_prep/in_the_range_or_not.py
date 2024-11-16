n=int(input())
arr=[]
for i in range(0,n):
    a=int(input())
    arr.append(a)
for i in arr:
    if i>=67 and i<=45000:
        print("YES")
    else:
        print("NO")
