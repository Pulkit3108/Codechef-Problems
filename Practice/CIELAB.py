# cook your dish here
A,B=map(int,input().split())
C=int(A-B)
if(C%10==9):
    print(C-1)
else:
    print(C+1)



