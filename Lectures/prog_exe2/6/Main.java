class Student {
    String name;
    int height;
    int weight;

    Student(String name, int height, int weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    void print() {
        System.out.printf("name:%s height:%d, weight:%d\n", name, height, weight);
    }
}

class Gakyu {
    String name;

    Student[] students;

    // num_student:生徒の数
    Gakyu(int num_student) {
        students = new Student[num_student]; // Studentの配列のインスタンス

        // 生徒の情報を作成する（生徒のインスタンスを作る）
        students[0] = new Student("taro", 160, 60);
        students[1] = new Student("jiro", 170, 160);
        students[2] = new Student("saburo", 180, 50);

    }

    public int Ave() {
        return (students[0].height + students[1].height + students[2].height) / 3;
    }
}
    




public class Main {
    public static void main(String[] args) {
        /*Student taro = new Student("taro", 160, 60);
        Student jiro = new Student("jiro", 170, 160);
        Student saburo = new Student("saburo", 180, 50);

        taro.print();
        jiro.print();
        saburo.print();
        */

        Gakyu ai = new Gakyu(3);
        int i = ai.Ave();
        System.out.println(i);
        ai.name = "sinobu";

        System.out.println(ai.name);
    }
}


    

