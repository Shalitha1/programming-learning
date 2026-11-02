#include <stdio.h>

// Function to display array elements using a pointer
void display(int *ptr, int n) {

    int i;

    for (i = 0; i < n; i++) {
        printf("%d ", *(ptr + i));
    }

}

int main() {

    int arr[10];
    int i;

    // Input 10 integers
    printf("Enter 10 integers:\n");

    for (i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
    }

    // Pass array to function
    display(arr, 10);

    return 0;
}