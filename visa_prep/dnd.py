a,b=map(int,input().split())
arr=list(map(int,input().split()))
div=0
ndiv=0
for i in arr:
    if i%b==0:
        div+=i
    else:
        ndiv+=i
res=div-ndiv
print(res)
    
