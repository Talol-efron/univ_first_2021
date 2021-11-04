#include <stdio.h>
#include <assert.h>

int main(void)
{

    int data[] = {4, 7, 5, 3, 7, 4, 4, 234, 65, 32, 3, 9, 0};
    const int len_data = sizeof(data) / sizeof(int);

    int max_value = 0; //配列の要素が全て正の整数である前提
    int i,j = 0;
    /*
ここに最大値を求めて，max_valueに代入するコードを書く
*/
    for (i = 0; i < len_data; i++)
    {
        assert(i >= 0 && i < len_data);

        for (j = i + 1; j < len_data; j++)
        {
            assert(j >= 1 && j < len_data);
            if (data[i] < data[j])
            {
                data[i] = data[j];
            }
        }
    }
    max_value = data[0];
    printf("maximum value = %d\n", max_value);

    return 0;
}
