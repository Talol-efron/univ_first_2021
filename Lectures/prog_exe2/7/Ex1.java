import java.util.ArrayList;

class Student{
    String name;
    int math;
    int English;
    int Japanese;

    Student(String name,int math,int English,int Japanese){
        this.name = name;
        this.math = math;
        this.English = English;
        this.Japanese = Japanese;
    }

    int total(){
        return math + English + Japanese;
    }
}

class Gakyu{
    String teacherName;
    ArrayList<Student> students;

    Gakyu(){
        students = new ArrayList<>();
    }

    int aveJapanese(){
        int sum = 0;
        for (var s : students){
            sum += s.Japanese;
        }
        return sum / students.size();
    }

    int aveEnglish() {
        int sum = 0;
        for (var s : students) {
            sum += s.English;
        }
        return sum / students.size();
    }

    int aveMath() {
        int sum = 0;
        for (var s : students) {
            sum += s.math;
        }
        return sum / students.size();
    }

    int aveAll(){
        int sum = 0;
        for (var s : students){
           sum += s.total();
        } 
        return sum / students.size();
    }

    void printSammary(){
        System.out.println(teacherName + "学級のメンバーは");
        for (var s :students){
            System.out.println(s.name + " ");
        }
        System.out.println();
        System.out.println("生徒の国語の平均点は" + aveJapanese());
        System.out.println("生徒の英語の平均点は" + aveEnglish());
        System.out.println("生徒の数学の平均点" + aveMath());
        System.out.println();
        System.out.println("生徒の３科目合計の平均は" + aveAll());
    }
}
public class Ex1{
    public static void main(String[] args) {
        var student1 = new Student("Taro",  100, 25, 30);
        var student2 = new Student("Miyu", 60, 80, 70);
        var student3 = new Student("Ippei", 80, 100, 60);
        
        var gakyu1 = new Gakyu();
        gakyu1.teacherName = "うんこ";
        gakyu1.students.add(student1);
        gakyu1.students.add(student2);    
        gakyu1.students.add(student3); 

        gakyu1.printSammary();
    }
}