/*WAP to implement Money Change Problem*/
#include<stdio.h>

int main()
{
    int coins[10], n, amount;
    printf("Enter number of coin types: ");
    scanf("%d", &n);

    printf("Enter coin denominations: ");
    for(int i=0; i<n; i++)
    {
        scanf("%d", &coins[i]);
    }

    printf("Enter the amount: ");
    scanf("%d", &amount);

    long long dp[1000] = {0};   // dp[i] = number of ways to make amount i
    dp[0] = 1;                  // base case: 1 way to make 0

    // Dynamic Programming approach
    for(int i=0; i<n; i++)
    {
        for(int j=coins[i]; j<=amount; j++)
        {
            dp[j] += dp[j - coins[i]];
        }
    }

    printf("Number of ways to make %d = %lld\n", amount, dp[amount]);

    return 0;
}
