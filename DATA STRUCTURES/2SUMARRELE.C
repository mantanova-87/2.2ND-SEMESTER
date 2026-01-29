/*PROGRAM TO FIND SUM OF ARRAY ELEMENTS.*/
#include<stdio.h>
int main()
{
    int N;
    printf("ENTER THE NUMBER OF ELEMENTS YOU WANT IN ARRAY: ");
    scanf("%d",&N);
    int ARR[N];
    int i;
    for ( i = 0; i < N; i++){
        int E;
        printf("ENTER THE ELEMENT TO ADD TO ARRAY: ");
        scanf("%d",&E);
        ARR[i]=E;}
    int SUM=0;
    for ( i = 0; i < N; i++){
        SUM=SUM+ARR[i];
    }
    printf("THE SUM OF ELEMENTS IN THE ARRAY IS: %d",SUM);
    
}