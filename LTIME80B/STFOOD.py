import math
T=int(input())
for k in range(0,T):
    N=int(input())
    S=[0]*N
    V=[0]*N
    P=[0]*N
    y=0
    for i in range(0,N):
        S[i],P[i],V[i]=map(int,input().split())
    for j in range(0,N):
        x=0
        x=math.floor(P[j]/(S[j]+1))
        x=x*V[j]
        y=max(y,x)
    print(y)
