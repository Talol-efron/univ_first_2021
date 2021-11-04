package EX;
class Student {
    String name;
    String department; // 所属学科
    String phone;
    String address;
    int credits;

    void acquireCredit(/* Student x */) { // staticはつけない，Student sもいらない
        // 暗黙に渡されたインスタンスはthisで参照できる．
        this.credits += 1;
    }

    boolean canGraduate() {
        int minCredits = 130;
        return this.credits >= minCredits;
    }
}

public class Exercise {
    public static void main(String args[]) {
        Student a = new Student();
        a.credits = 90;
        System.out.println(a.canGraduate());
    }
    
}
