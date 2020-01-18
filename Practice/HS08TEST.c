#include<stdio.h>
int main()
{ int x;
float y;
scanf("%d",&x);
scanf("%f",&y);
if(x>0&&x<=2000&&y>0&&y<=2000)
{
       if((x%5==0) && (x+0.5<y))
       {
              y=y-x-0.5;
       }
       printf("%.2f",y);
}
return 0;
}
