n=int(input())
a=-1 if n<0 else 1
n=abs(n)
rev=int(str(n)[::-1])
rev*=a
if rev<-2**31 or rev>2**31-1:
    print(0)
else:
    print(rev)
    
