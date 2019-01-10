#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<math.h>
#include<graphics>
#define SQUARE(x) ((x)*(x))
using namespace std;
void drawcircle(int ,int,int);
void main()

{
int gd,gm,err;
int xc,yc,r;
gd=DETECT;
initgraph(&gd,&gm,"\\tc\\bgi");
err=graphresult();
if(err!=0)
{
printf("ERROR:%s",grapherrormsg(err));
printf("\nPress a key..");
getch();
exit(1);
}
xc=getmaxx()/2;
yc=getmaxy()/2;
r=50;
drawcircle(xc,yc,r);
getch();
closegraph();
return 0;
}*///end main
void drawcircle(int xc,int yc,int r)
{
int i,x,y,y1;
for(i=xc-r;i<=xc+r;i++)
{
x=i;
y=yc+sqrt(SQUARE(r)-SQUARE(x-xc));
y1=yc-sqrt(SQUARE(r)-SQUARE(x-xc));
putpixel(x,y,1);
putpixel(x,y1,1);
}
