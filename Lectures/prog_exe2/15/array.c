#include <stdio.h>
#include <assert.h>

void printArray(const char *name, int *arr, int len)
{
    for (int i = 0; i < len; i++)
    {
        printf("%s[%d] = %d\n", name, i, arr[i]);
    }
}

int main(void)
{

    const int LEN = 5;

    int arr1[LEN] = {0, 1, 2, 3, 4};
    int arr2[LEN] = {5, 6, 7, 8, 9};

    for (int i = 0; i < LEN * 2; i++)
    {
        assert(i >= 0 && i < LEN);

        arr2[i] = i * 10;

        printArray("arr1", arr1, LEN);
        printArray("arr2", arr2, LEN);

        return 0;
    }
}