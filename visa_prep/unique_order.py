n=int(input())
a=map(int,input().split())
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end=" ")
