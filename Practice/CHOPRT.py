# cook your dish here
T=int(input())
for i in range(0,T):
    A,B=map(int,input().split())
    if(A>B):
        print(">")
    elif(A<B):
        print("<")
    else:
        print("=")
