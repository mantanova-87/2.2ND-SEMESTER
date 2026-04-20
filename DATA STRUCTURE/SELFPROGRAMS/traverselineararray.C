#include<stdio.h>
int main()
{
    int N;
    printf("How many elements do you wish to enter in array");
    scanf("%d",&N);
    int ARR[N];int i;
    for ( i = 0; i < N; i++)
    {
        int E;
        printf("Enter the element to create array: ");
        scanf("%d",&E);
        ARR[i]=E;     
    }
    printf("LET'S TRAVERSE THE ARRAY!!!\n");
    for ( i = 0; i < N; i++)
    {
        int A=ARR[i];
        printf("%d \n",A);
    }
    
    
}