#include <iostream>
using namespace std;
void bubbleSort(int A[], int N)
{                 // N 個の要素を含む 0-オリジンの配列 A
    int flag = 1; // 逆の隣接要素が存在する
    int hoge;
    int num = 0;
    while (flag == 1)
    {
        flag = 0;
        for (int j = N - 1; j > 0; j--)
        {
            if (A[j] < A[j - 1])
            {
                hoge = A[j];
                A[j] = A[j - 1];
                A[j - 1] = hoge;
                flag = 1;
                num++;
            }
        }
    }
    for (int k = 0; k < N; k++)
    {
        cout << A[k] << " ";
    }
    cout << " " << endl;

    cout << num << endl;
}

int main()
{
    int NUM[] = {5, 1, 8, 0, 2, 5, 8};
    int size;
    size = sizeof(NUM) / sizeof(*NUM);
    bubbleSort(NUM, size);
    return 0;
}