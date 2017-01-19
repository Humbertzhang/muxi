#include<stdio.h>

int main(void)
{
    int n , counter=0;
    scanf("%d",&n);
    while (n != 1)
        if (n%2 == 0)
            {
            n = n/2;
            counter = counter + 1;
            }
        else
        {
            n = (3*n+1)/2;
            counter = counter + 1;
        }
    printf("%d",counter);
    return 0;
}
