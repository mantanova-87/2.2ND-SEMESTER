/*WAP to find the sum of array elements*/
#include<stdio.h>
int main()
{
    int N;
    printf("ENTER THE NUMBER OF ELEMENTS YOU WANT IN YOUR ARRAY: ");
    scanf("%d",&N);
    int ARR[N],i,S=0;
    for ( i = 0; i < N; i++)
    {
        int A;
        printf("Enter the number to create array: ");
        scanf("%d",&A);
        ARR[i]=A;
    }
    for ( i = 0; i < N; i++)
    {
        S+=ARR[i];
    }
    printf("The sum of all the elements of array is %d",S);    
}