T=int(input())
for i in range(0,T):
       n=int(input())
       s=0
       while(n!=0):
              r=int(n%10)
              n=int(n/10)
              s=s+r
       print(s)
