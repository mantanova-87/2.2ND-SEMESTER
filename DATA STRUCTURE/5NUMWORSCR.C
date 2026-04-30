/*WAP to print the numbers of ways a given word can be scrambled*/
#include<stdio.h>
int main()
{
    char STR[25];
    printf("Enter the string: ");
    scanf("%s", STR);

    int LEN=0;
    while(STR[LEN]!='\0')   
    {
        LEN++;
    }

    int FREQ[256]={0};
    for(int i=0;i<LEN;i++)
    {
        FREQ[(unsigned char)STR[i]]++;
    }

    long long NUM=1;
    for(int i=2;i<=LEN;i++)
    {
        NUM*=i;   
    }

    long long DEN=1;
    for(int i=0;i<256;i++)
    {
        if(FREQ[i]>1)
        {
            long long TEMP=1;
            for(int j=2;j<=FREQ[i];j++)
            {
                TEMP*=j;   
            }
            DEN*=TEMP;
        }
    }

    long long WAYS=NUM/DEN;
    printf("Number of ways the word can be scrambled: %lld\n",WAYS);

    return 0;
}
