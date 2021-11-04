#include <iostream>
#include <algorithm>
using namespace std;

int main(){
   int x, y; //x,yはともに入力数値(cin を用いる？)
   cin >> x >> y;
   int ans;
   if (x > y){
      ans = x % y;
      // x ≥ y ならば x と y の最大公約数は y と x % y の最大公約数に等しい
      while (ans != 0){
      x = y;
      y = ans;
      ans = x % y;
      }
      cout << y;
   }else if (x < y){
      ans = y % x;
      while (ans != 0)
      {
      y = x;
      x = ans;
      ans = y % x;
      }
      cout << x;
   }else{
      cout << x;
   }

   return 0;
}