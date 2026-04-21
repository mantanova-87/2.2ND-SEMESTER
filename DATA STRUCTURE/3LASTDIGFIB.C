/*WAP to print the Last Digit of a Large Fibonacci Number*/
#include<stdio.h>
int main()
{   
    int A=0,B=1,F,i;
    printf("Last digit of which term of the fibonacci series you want? ");
    scanf("%d",&F);
    for ( i = 0; i < F-2; i++)
    {
        int D=A+B;
        A=B;
        B=D;
    }
    printf("The %d th term of the fibonacci series is: %d\n",F,B);
    if (B>=10 || B<=-10)
    {
        printf("The last digit of %d th term of the fibonacci series is: %d",F,(B%10)); 
    }
    else if (B>-10 && B<10 )    
    {
        printf("The %d th term of the fibonacci series is not a large number.",F);

    }
}