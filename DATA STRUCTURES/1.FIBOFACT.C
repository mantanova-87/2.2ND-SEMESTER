#include<stdio.h>
int main()
{
    printf("ENTER 1 TO CALCULATE THE FACTORIAL OF A NUMBER.\nENTER 2 TO PRINT GIVEN NUMBER OF TERMS OF  FIBONACCI SERIES");
    int CH;
    char I;
    scanf("PLEASE ENTER YOUR CHOICE: ",&CH);
    
    while (I=="YES")
    {

        printf("ENTER YES IF YOU WISH TO CONTINUE AND ENTER SOMETHING ELSE TO EXIT THE PROGRAM.");
        scanf("ENTER YOUR CHOICE: "&I);
        if (CH==2)
        {
            int A,B=0,C=1,D,S;
            printf("ENTER THE NUMBER OF TERMS OF FIBONACCI SERIES YOU WANT TO PRINT: ");
            scanf("%d",&A);
            printf("FOLLOWING IS THE REQUIRED FIBONACCI SERIES: \n");
            printf("%d ",B);
            for ( int I=0; I<=A-2; I++)
            {
                B=C;
                C=S;
                S=B+C;
                printf("%d  ",S);
            }
        }
        els
        
    }
    

}