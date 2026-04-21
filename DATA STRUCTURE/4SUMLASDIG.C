/*WAP to print the Last Digit of the Sum of Fibonacci Numbers*/
#include<stdio.h>
int main()
{
    int A=0,B=1,F,i,S=1;
    printf("Last digit of sum of how many first terms is required? ");
    scanf("%d",&F);
    for ( i = 0; i < F-2; i++)
    {
        int D=A+B;
        S=S+D;
        A=B;
        B=D;
    }
    printf("THE LAST DIGIT OF SUM OF FIRST %d  TERMS OF FIBONACCI SERIES IS: %d ",F,(S%10));
}