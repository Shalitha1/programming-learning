#include<stdio.h>

int main (){
    int arr[10];
    int i;
    printf("Enter 10 integers for the array:");

    for(i=0; i<10;i++){
        scanf("%d", &arr[i]);
    }

    printf("Integeres:");
    for(i=0; i<10; i++){
        printf("%d", arr[i]);
    }
    return 0;


}