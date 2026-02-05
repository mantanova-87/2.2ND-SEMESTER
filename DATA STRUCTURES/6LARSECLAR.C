/*WAP TO FIND THE LARGEST AND SECOND LARGEST ELEMENT OF AN ARRAY.*/
#include<stdio.h>
int main()
{
    int N;
    printf("ENTER THE NUMBER OF ELEMENTS TO STORE IN ARRAY: ");
    scanf("%d",&N);
    int ARR1[N];
    int i;
    for ( i = 0; i < N; i++)
    {
        int a;
        printf("ENTER THE ELEMENT: ");
        scanf("%d",&a);
        ARR1[i]=a;
    }
    int MAX1=ARR1[0],MAX2=ARR1[0];
    for ( i = 1; i < N; i++)
    {
        if (ARR1[i]>MAX1)
        {
            MAX1=ARR1[i];
            
        }
        if (ARR1[i]>MAX2 && ARR1[i]<MAX1)
        {
            MAX2=ARR1[i];
        }
        
    }
    printf("THE LARGEST AND SECOND LARGEST ELEMENTS IN THE ARRAY ARE %d and %d.\n",MAX1,MAX2);
}