# cook your dish here
import math
T=int(input())
for i in range(0,T):
    n=int(input())
    count=0
    i=5
    while(int(n/i)>=1):
        count+=int(n/i)
        i=int(i*5)
    print(int(count))
