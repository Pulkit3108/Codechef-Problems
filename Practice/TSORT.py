n=int(input())
a=[0]*n
for i in range(0,n):
    x=int(input())
    a[i]=x
a.sort()
for i in range(0,len(a)):
       print(a[i])
