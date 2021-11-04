#include <stdio.h>

int main(void)
{

    const int LEN = 5;

    int arr1[LEN] = {0, 1, 2, 3, 4};
    int arr2[LEN] = {5, 6, 7, 8, 9};

    printf("sizeof(arr1)= %lu\n", sizeof(arr1));
    printf("sizeof(int)= %lu\n", sizeof(int));

    return 0;
}
