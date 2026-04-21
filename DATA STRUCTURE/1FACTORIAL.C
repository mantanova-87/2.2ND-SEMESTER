/*1	WAP to print the factorial of a given number.*/
#include<stdio.h>
int main()
{
    int N,F=1;
    printf("Enter the integer to find its facorial: \n");
    scanf("%d",&N);
    if (N==0)
    {
        printf("The factorial of 0 is 1.");
    }
    else if (N<0)
    {
        printf("The factorial of negative numbers isn't defined.");    
    }
    else
    {
       while (N>0) 
       {
            F=F*N;
            N-=1;
        }
        printf("%d\nTHe factorial of the entered number isL: ",F);
    }
}