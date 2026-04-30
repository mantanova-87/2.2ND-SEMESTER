/*WAP to insert a new element at a given location in an array.Insert 10 at location 3.*/
#include<stdio.h>
int main()
{
    int ARR[10]={1,2,3,4,5};
    int N=5,POS=3,ELE=10;
    if (POS<1 || POS>N+1)
    {
        printf("INVALID POSITION.\n");
    }
    else if (POS>1 && POS<=N+1)
    {
        for (int i = N-1; i==N-POS ; i--)
        {
            ARR[i+1]=ARR[i];
        }
        ARR[POS-1]=ELE;
        for (int i = 0; i < N+1; i++)
        {
            printf("%d ",ARR[i]);
        }         
    }  
}