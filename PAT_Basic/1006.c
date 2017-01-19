#include<stdio.h>
int main(void)
{
    int n;
    int i=0,j=0,k=0;
    scanf("%d",&n);
    i = n / 100;
    n = n - i*100;
    for (i;i>0;i--)
        printf("B");
    j = n / 10;
    n = n -j*10;
    for (j;j>0;j--)
        printf("S");
    k = 0;
    for (k;k<=n;k++)
        printf("%d",k+1);
    return 0;
}

