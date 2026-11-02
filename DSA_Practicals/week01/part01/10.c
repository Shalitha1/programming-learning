#include<stdio.h>

int main(){
    int num =50;
    int *ptr;

    ptr = &num;

    printf("%d\n", num);

    printf("%p\n", &num);

    printf("%d\n", *ptr);

    return 0;
}

