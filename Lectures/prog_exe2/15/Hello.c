#include <stdio.h>

int main(void)
{

    int value = 4;
    char str[] = "mojiretsu";

    printf("value = %d, str = %s\n", value, str);
    //%d(整数,int),%s(文字列,char[])の順で出現するので，第２引数に整数,次に文字列を渡す
    printf("hello world!\n");
    return 0;
}
