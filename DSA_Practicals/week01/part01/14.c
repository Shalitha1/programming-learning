#include<stdio.h>

int main(){
    int arr[10];
    int i, search, count =0;
    int *ptr;

    print("Enter 10 integers:\n");
    for(i=0; i<10; i++){
        scanf("%d", &arr[i]);
    }

    ptr = arr;

    printf("Enter a number to search:\n");
    scanf("%d", search);

    for(i=0; i<10; i++){
        if(*(ptr + 1) == search){
            count ++;
        }
    }
    printf("%d occurs %d times in the array\n", search, count);
    return 0;
}

