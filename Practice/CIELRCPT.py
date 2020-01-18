#cook your dish here
T=int(input())
for i in range(0,T):
    n=int(input())
    count=0
    while(n>2048):
           n=n-2048
           count+=1
    b=str(bin(n))
    print(b.count('1')+count)
    
