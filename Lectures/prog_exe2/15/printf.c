#include <stdio.h>

int main(void)
{

    int a = 4;
    int b = 3;
    char str[] = "string";

    /* 
    a,bの値，及びaとbを乗算した結果をprintfで出力
    strの文字列をprintfで出力
    */
   printf("a = %d\n",a);
   printf("b = %d\n",b);
   printf("a * b = %d\n", a*b);
   printf("str = %s\n", str); 
   return 0;
}
