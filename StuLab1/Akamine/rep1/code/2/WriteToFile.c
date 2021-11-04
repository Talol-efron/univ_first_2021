#include <stdio.h>

int main(void)
{
    FILE *f = fopen("out_c.txt", "w"); //pythonではwith open

    for (int i = 0; i < 1000 * 1000 * 10; ++i)
    {
        fprintf(f, "%d", i);
    }

    fclose(f);

    return 0;
}
