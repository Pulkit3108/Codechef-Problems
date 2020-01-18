N=int(input())
s=input()
a=s[0]
l=1
for i in range(N):
    for j in range(i+1,N+1):
        c=s[i:j]
        if(c==''.join(reversed(c)) and len(s[i:j])>l):
            a=s[i:j]
            l=len(a)
print(l)
print(a)
    
