#include <stdio.h>

int main(void)
{

    char str2[] = "test";
    char str[] = "foge";
    str[4] = 'a';
    printf("str = %s\n", str);
    printf("str2= %s\n", str2);

    return 0;
}
