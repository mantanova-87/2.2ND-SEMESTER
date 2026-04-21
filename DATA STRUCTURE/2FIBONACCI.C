/*WAP to print the Fibonacci series*/
#include<stdio.h>
int main()
{
    int C;
    printf("Enter 1 if you want the general conventional fibonacci series.\nEnter 2 if you want custom fibonacci series.\n");
    scanf("%d",&C);
    if (C==1)
    {
        int A=0,B=1,F,i;
        printf("How many terms do you want in the fibonacci series? ");
        scanf("%d",&F);
        printf("%d\n",A);
        printf("%d\n",B);
        for ( i = 0; i < F-2; i++)
        {
           int D=A+B;
           printf("%d\n",D);
           A=B;
           B=D;
        }      
    }
    else if (C==2)
    {
        int A,B,C,F,i;
        printf("How many terms do you want in the fibonacci series? ");
        scanf("%d",&F);
        printf("Enter the smaller of the starting two numbers of your fibonnaci series: ");
        scanf("%d",&A);
        printf("Enter the larger of the starting two numbers of your fibonacci series: ");
        scanf("%d",&B);
        printf("%d\n",A);
        printf("%d\n",B);
        for ( i = 0; i < F-2; i++)
        {
           int D=A+B;
           printf("%d\n",D);
           A=B;
           B=D;
        }      
    }     
}