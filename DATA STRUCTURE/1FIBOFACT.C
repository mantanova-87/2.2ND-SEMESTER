#include<stdio.h>
int main()
{
    char I;
    while (I='Y')
    {
        int CH;
        printf("ENTER 1 TO CALCULATE THE FACTORIAL OF A NUMBER.\nENTER 2 TO PRINT GIVEN NUMBER OF TERMS OF  FIBONACCI SERIES\n");
        scanf("%d",&CH);
        if (CH==2)
        {
            int A,B=0,C=1,S;
            printf("ENTER THE NUMBER OF TERMS OF FIBONACCI SERIES YOU WANT TO PRINT: ");
            scanf("%d",&A);
            printf("FOLLOWING IS THE REQUIRED FIBONACCI SERIES: \n");
            printf("%d ",B);
            int SUM=
            for ( int I=0; I<=A-2; I++)
            {
                B=C;
                C=S;
                S=B+C;
                printf("%d  ",S);
            }
        }
        if (CH==1)
        {
            int A;
            printf("ENTER THE NUMBER TO FIND ITS FACTORIAL:");
            scanf("%d",&A);
            if (A==0 || A==1)
            {
                printf("FACTORIAL OF %d IS 1.",A);
            }
            else if (A<0)
            {
                printf("FACTORIAL OF NEGATIVE NUMBERS IS NOT DEFINED.");
            }
            else
            {
                int i,F=1;
                for ( i = A; i >0; i--)
                {
                    F*=i;
                }
                printf("FACTORIAL OF %d IS %d.",A,F);
            }   
          
        }
        char Z;
        printf("\nENTER Y IF YOU WISH TO CONTINUE AND ENTER SOMETHING ELSE TO EXIT THE PROGRAM: \n");
        scanf(" %c",&Z);
        if (Z!='Y')
        {
                break;
        }        
    }
}