#include<stdio.h>

void display(int *ptr, int n){
    int i;
    for(i=0; i<n; i++){
        printf("%d", *(ptr+1));
    }
}

int main(){
    int arr[10];
    int i;

    printf("10 integers:\n");
    for(i=0; i<10; i++){
        scanf("%d", &arr[i]);
    }

    display(arr, 10);

    return 0;
}


