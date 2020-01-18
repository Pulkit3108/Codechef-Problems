
T=int(input())
for i in range(0,T):
       n=int(input())
       x=int(n%10)
       while(n!=0):
              y=int(n/10)
              if(y!=0):
                     n=int(n/10)
              else:
                     z=x+n
                     print(z)
                     break;
                     
       
       
