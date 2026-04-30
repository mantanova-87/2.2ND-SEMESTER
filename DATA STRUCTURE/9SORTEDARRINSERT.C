/*WAP to insert a new element in the sorted array*/
#include<stdio.h>
int main()
{
    int N;
    printf("ENTER THE NUMBER OF ELEMENTS TO INSERT TO FORM SORTED ARRAY: ");
    scanf("%d",&N);
    int ARR[N+1];int i;
    printf("Enter the elements in ascending or descending order to create the sorted array: ");
    for ( i = 0; i < N; i++)
    {
        scanf("%d",&ARR[i]);
    }
    int CH;
    printf("Enter 1 if the sorted array is in ascending order.\nEnter 2 if the sorted array is in descending order.\n");
    scanf("%d",&CH);
    int E;
    printf("Enter the element to be inserted in the sorted array.");
    scanf("%d",&E);
    if (CH==1)
    {
        int LOC;
        for ( i = 0; i <N; i++)
        {
            if (ARR[i]<=E && ARR[i+1]>=E)
            {
                LOC=i+1;
            }
        }
        printf("%d\n",LOC);
        for ( i = N; i >LOC; i--)
        {
            ARR[i]=ARR[i-1];
        }
        ARR[LOC]=E;
        for ( i = 0; i < N+1; i++)
        {
            printf("%d ",ARR[i]);
        }             
    }
    else if (CH==2)
    {
       int LOC;
        for ( i = 0; i <N; i++)
        {
            if (ARR[i]>=E && ARR[i+1]<=E)
            {
                LOC=i+1;
            }
        }
        printf("%d\n",LOC);
        for ( i = N; i >LOC; i--)
        {
            ARR[i]=ARR[i-1];
        }
        ARR[LOC]=E;
        for ( i = 0; i < N+1; i++)
        {
            printf("%d ",ARR[i]);
        }              
    }
    
    
}