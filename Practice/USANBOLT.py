import math
T=int(input())
for i in range(0,T):
    f,d,a,b=map(int,input().split())
    t1=f/b
    t2=math.sqrt(2*(f+d)/a)
    if(t1<t2):
        print("Bolt")
    else:
        print("Tiger")
    


