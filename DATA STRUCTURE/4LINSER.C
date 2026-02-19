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
    int E,C;
    printf("ENTER THE ELEMENT TO BE SEARCHED IN THE ARRAY: ");
    scanf("%d",&E);
    int flag=0;
    for ( i = 0; i < N; i++)
    {
        if (ARR1[i]==E)
        {
            C=i;
            flag=1;
        }    
    }
    if (flag==1)
    {
        printf("THE ELEMENT EXISTS AT INDEX %d IN THE ARRAY.",C);
    }
    else
    {
        printf("THE ELEMENT DOES NOT EXIST IN THE ARRAY.");
    }
    
    
    
    



    
}