N=int(input())
a=0
b=0
A=[]
B=[]
for i in range(0,N):
    T1,T2=map(int,input().split())
    a=a+T1
    b=b+T2
    A.append((abs(a-b)))
    if(a>b):
        B.append((1))
    else:
        B.append((2))
C=A.index((max(A)))
print(B[C],A[C])
