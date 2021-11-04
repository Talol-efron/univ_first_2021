import java.util.ArrayList;

class Employee {
    String name;
    int salary;
    int sales;

    Employee(String name, int salary, int sales) {
        this.name = name;
        this.salary = salary;
        this.sales = sales;
    }

    int calcAnnualIncome() {
        return salary * 16; // 12+ボーナス四ヶ月
    }
}

class Section {
    String name;
    Employee representation;
    ArrayList<Employee> members;

    Section() {
        members = new ArrayList<>();
    }

   int meanSalary() {
       int sum = 0;
       for(var m : members) {
           sum += m.salary;
       }
       return sum / members.size();
   }

   int sumSales() {
       int sum = 0;
       for(var m : members) {
           sum += m.sales;
       }
       return sum;
       }

   int meanAnnualIncome() {
       int sum = 0;
       for (var m : members) {
           sum += m.calcAnnualIncome();
       }
       return sum / members.size();
   }

   // テスト用コード
   void printSammary() {
       System.out.println(name + "の");
       System.out.print("メンバーは");
       for (var m : members) {
           System.out.print(m.name + " ");
       }
       System.out.println();
       System.out.print("平均月収は");
       System.out.print(meanSalary());
       System.out.println();
       System.out.print("平均合計売り上げは");
       System.out.print(sumSales());
       System.out.println();
       System.out.print("メンバーの平均年収は");
       System.out.print(meanAnnualIncome());
       System.out.println();
   }
}

public class Main {
    public static void main(String[] args) {
        var section1 = new Section(); //部署のインスタンス生成
        section1.name = "営業１課"; //部署名を代入

        //代表者のインスタンスを代入（インスタンス = 社員一人　を表す)
        section1.representation = new Employee("kacho", 500000, 1000000);
        /*
        * Employee(String name, int salary, int sales) { this.name = name; this.salary
        * = salary; this.sales = sales; }
        */
        var employee1 = new Employee("taro", 200000, 500000);

        // section1.members は，ArrayListのインスタンス
        // ArrayListで末尾に追加するには，addメソッドを使う．引数が追加するインスタンス
        section1.members.add(employee1);

        section1.members.add(new Employee("jiro", 300000, 600000));

        // section1.representationはEmployeeのインスタンスなのでaddできる．
        section1.members.add(section1.representation);

        var section2 = new Section();
        section2.name = "営業２課";
        section2.representation = new Employee("shachosan", 450000, 900000);
        section2.members.add(section2.representation);
        section2.members.add(new Employee("saburo", 200000, 400000));
        section2.members.add(new Employee("shiro", 250000, 300000));

        section1.printSammary();
        section2.printSammary();
    }
}
