/*IMPLEMENTING PUSH AND POP OPERATIONS ON STACK USING ARRAY */
#include<stdio.h>
#define MAX 5

int stack[MAX];
int top = -1;  
void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow! Cannot push %d\n", value);
    } else {
        top++;
        stack[top] = value;
        printf("%d pushed into stack\n", value);
    }
}

int pop() {
    if (top == -1) {
        printf("Stack Underflow! Cannot pop\n");
        return -1;
    } else {
        int value = stack[top];
        top--;
        printf("%d popped from stack\n", value);
        return value;
    }
}

int main() {
    int N;
    printf("ENTER THE NUMBER OF VALUES TO PUSH TO STACK: ");
    scanf("%d",&N);
    int i=0;
    for (size_t i = 0; i < N; i++)
    {
        int Z;
        printf("ENTER THE VALUE TO PUSH TO STACK: ");
        scanf("%d",&Z);
        push(Z);

    }
    pop();
    return 0;
}
