n=int(input())
arr=list(map(int,input().split()))
temp=arr[0]
for i in range(0,n-1):
    arr[i]=arr[i+1]
arr[n-1]=temp
for i in arr:
    print(i,end=" ")
