package Example1;
class Student {
    String name;
    String department; // 所属学科
    String phone;
    String address;
    int credits;

    void acquireCredit() { // staticはつけない，Student sもいらない
        // 暗黙に渡されたインスタンスはthisで参照できる．
        this.credits += 1;
    }
};

public class Example4 {
    public static void main(String args[]) {
        Student a = new Student();
        Student b = new Student();
        a.credits = 80;
        b.credits = 90;

        a.acquireCredit();
        a.acquireCredit();
        b.acquireCredit();

        System.out.println("a.credits = " + a.credits);
        System.out.println("b.credits = " + b.credits);
    }
}
