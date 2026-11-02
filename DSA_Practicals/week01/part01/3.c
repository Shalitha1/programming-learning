#include<stdio.h>

int main(){
    int arr[10];
    int i, largest, smallest;

    printf("Enter 10 integers:\n");

    for (i=0; i<10;i++){
        scanf("%d", &arr[i]);
    }

    largest = arr[0];
    smallest = arr[0];

    for(i=0; i<10; i++){
        if(arr[i] > largest){
            largest = arr[i];
        }
        if(arr[i] < smallest){
            smallest = arr[i];
        }
    }
    printf("Largest element is: %d\n", largest);
    printf("Smallest element is: %d\n", smallest);

    return 0;
    
}

