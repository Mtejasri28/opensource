n=int(input())
a=list(map(int,input().split()))
rev=a[::-1]
for i in rev:
    print(i,end=" ")
