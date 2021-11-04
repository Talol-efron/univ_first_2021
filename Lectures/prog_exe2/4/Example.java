class Student {
    String name;
    String department; // 所属学科
    String phone;
    String address;
    int credits;
};

public class Example {
    public static void main(String args[]){
        Student a = new Student(); //インスタンスの生成（印刷）
        Student b = new Student(); 
        Student c = b; //参照のコピー (シリアル番号だけ書き写す）

        a.credits = 80; //aさんは80単位 
        b.credits = 90; //bさんは90単位
        c.credits = 0;

        System.out.println("a.credits = " + a.credits);
        System.out.println("b.credits = " + b.credits); //90のはず
        System.out.println("c.credits = " + c.credits);

    }
}
