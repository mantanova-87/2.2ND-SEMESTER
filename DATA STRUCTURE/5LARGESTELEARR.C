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
    int MAX=ARR1[0];
    int LOC=0;
    for ( i = 1; i < N; i++)
    {
        if (ARR1[i]>MAX)
        {
            MAX=ARR1[i];
            LOC=i;
        }
    }
    printf("THE LARGEST ELEMENT IN THE ARRAY IS %d .\n",MAX);
    printf("THE INDEX OF THE LARGEST ELEMENT IN THE ARRAY IS %d .",LOC); 
}