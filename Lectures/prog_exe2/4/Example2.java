public class Example2 {

    // 加算関数
    static int add(int a1, int a2) {
        return a1 + a2;
    }

    // mainメソッドは必ず以下のように宣言する
public static void main(String args[]){
        int a = 1;
        int b = 2;
        int c;
        c = add(a,b);
        System.out.println(a + "+" + b + "=" + c);
    }

}
