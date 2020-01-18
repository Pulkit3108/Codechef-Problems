#include<iostream>
#include<math.h>
#include<stdio.h> 
#include<stdlib.h> 
using namespace std;
int main()
{
    long int T,N,n,A,B,C,D,E,x,S;
    cin>>T;
    while(T--)
    {
       cin>>N;
       n=pow(10,N);
       cin>>A;
       S=(2*n)+A;
       cout<<S<<endl;
       fflush(stdout);
       cin>>B;
       C=n-B;
       cout<<C<<endl;
       fflush(stdout);
       cin>>D;
       E=n-D;
       cout<<E<<endl;
       fflush(stdout);
       cin>>x;
       if(x==-1)
       {
           exit(1);
       }
       
       
    }
    return 0;
}
