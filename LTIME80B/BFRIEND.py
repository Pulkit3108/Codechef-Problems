T=int(input())
for k in range(0,T):
    N,a,b,c=map(int,input().split())
    F=list(map(int,input().split()))
    minx = 10000000000000000000000000000000000000000000; 
    for i in range(0,len(F)):
        minx = min(minx,abs(a-F[i])+abs(b-F[i]))
    print(c+minx)
