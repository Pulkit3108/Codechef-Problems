T=int(input())
for i in range(0,T):
    S,W1,W2,W3=map(int,input().split())
    W=[]
    W.append(W1)
    W.append(W2)
    W.append(W3)
    c=0
    j=0
    count=1
    while(j<len(W)):
        c=c+W[j]
        if(c>S):
            count=count+1
            c=0
        else:
            j=j+1
    print(count)
            
            
        
