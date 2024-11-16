n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    count=0
    count=arr.count(i)
    if count==1:
        print(i)
