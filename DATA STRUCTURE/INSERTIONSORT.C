#include <stdio.h>

int main() {
    int arr[5] = {30, 10, 50, 20, 40};
    int i, j, key;

    // Insertion Sort
    for (i = 1; i < 5; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }

        arr[j + 1] = key;
    }

    // Print sorted array
    printf("Sorted array:\n");
    for (i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}