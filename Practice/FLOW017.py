# cook your dish here
T=int(input())
for i in range(0,T):
       a=list(map(int,input().split()))
       a.sort()
       print(a[1])
