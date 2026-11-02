
#include <stdio.h>

int main(){
    int arr[10];
    int i, search, found =0;

    printf("Input 10 integers:\n");
    for(i=0; i<10; i++){
        scanf("%d", &arr[i]);
    }

    printf("Enter the number needs to search: \n");
    scanf("%d", &search);

    for(i=0; i<10; i++){
        if(arr[i] == search){
            found = 1;
            break;
        }
    }

    if(found == 1){
        printf("%d found at position %d\n", search, i+1);
    } else {
        printf("%d didn't found\n", search);
    }

    return 0;

}
