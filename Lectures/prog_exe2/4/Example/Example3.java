package Example;
class Student {
    String name;
    String department; // 所属学科
    String phone;
    String address;
    int credits;
}

public class Example3 {
    // 単位を取得したよ
    static void acquireCredit(Student s) { // (4)
        s.credits += 1; // (5)
    }

    public static void main(String args[]) {
        Student a = new Student(); // (1)
        Student b = new Student(); // (6)
        a.credits = 80; // (2)
        b.credits = 90;

        acquireCredit(a); // (3)
        acquireCredit(a);
        acquireCredit(a);

        System.out.println("a.credits = " + a.credits);
        System.out.println("b.credits = " + b.credits);
    }
}
    

