#include<stdio.h>

int main(){
    int arr[10];
    int i, j, temp;

    printf("Enter 10 integeres:\n");
    for(i=0; i<10; i++){
        scanf("%d", &arr[i]);
    }
    
    for (i=0; i<9;i++){
        for(j=0; j<9; j++){
            if(arr[j] > arr[j+1]){
                temp = arr[j+1];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    printf("Array in ascending order:\n");
    for(i=0;i<10;i++){
        printf("%d", arr[i]);
    }
    printf("\n");
    return 0;
}



