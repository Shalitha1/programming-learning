#include<stdio.h>

int main(){
    int arr1[5], arr2[5], sum[5];
    int i;
    int *ptr1, *ptr2, *ptr3;

    for(i=0; i<5; i++){
        scanf("%d", &arr1[i]);
    }
    for(i=0; i<5; i++){
        scanf("%d", &arr2[i]);
    }

    ptr1 = arr1;
    ptr2 = arr2;
    ptr3 = sum;

    for(i=0; i<5; i++){
        *(ptr3 + i) = *(ptr1 + i) + *(ptr2 + i);
    }

    for(i=0; i<5; i++){
        printf("%d", *(ptr3 +1));
    }
    return 0;
}

