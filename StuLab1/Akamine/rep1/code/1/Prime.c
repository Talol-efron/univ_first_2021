#include <stdio.h>

int main(int argc, char **argv)
{
    int x = 1;

    for (int i = 3; i < 1000 * 50; ++i)
    {
        int dividable = 0;
        for (int j = 2; j < i; ++j)
        {
            if (i % j == 0)
            {
                dividable = 1;
                break;
            }
        }

        if (dividable == 0)
        {
            x++;
        }
    }

    printf("The number of primes = %d\n", x);

    return 0;
}