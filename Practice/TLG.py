import math
n=int(input())
c=0
at=0
bt=0
x=0
y=0
for i in range(0,n):
       a,b=input().split()
       a=int(a)
       b=int(b)
       at=at+a
       bt=bt+b
       if(c<abs(at-bt)):
              x=at
              y=bt
              
       c=max(c,abs(at-bt))
if(x>y):
       print(1,c)
else:
       print(2,c)
