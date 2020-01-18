# cook your dish here
T=int(input())
for i in range(0,T):
       n=int(input())
       count=0
       while(n!=0):
              r=int(n%10)
              if(r==4):
                     count+=1
              n=int(n/10)
       print(count)
