
public class Test {
    // mainメソッドは必ず以下のように宣言する
    public static void main(String args[]) {   
        String str = "";
        for (int i=0; i<5; i++){
            str = str + "!";

        }
        System.out.println(str);
        

        int sum = 0;
        for(int i=0; i<10; i++){
            sum += i;
        }
        
        System.out.println(sum);

        for (int i=0; i<10; i++){
            if(i % 2 == 0){
                System.out.print(i);
            }
        }

    }
}
