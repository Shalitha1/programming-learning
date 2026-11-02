#include <stdio.h>

int main(){
    int a, b,temp;
    int *ptr1, *ptr2;

    printf("Enter two numbers:\n");
    scanf("%d %d", &a, &b);

    ptr1 = &a;
    ptr2 = &b;

    temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;

    printf("After swapping:\n");
    printf("s = %d\n", a);
    printf("s = %d\n", b);

    return 0;
}

