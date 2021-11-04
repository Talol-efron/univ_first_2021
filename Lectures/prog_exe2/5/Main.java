class BankAccount {
    public int number;
    public int balance;

    BankAccount(int number, int balance) {
        this.number = number;
        this.balance = balance;
    }

    // 入金処理
    void deposit(int amount) {
        this.balance += amount;
    }
}


public class Main{
    public static void main(String[] args) {
        BankAccount a1 = new BankAccount(10,10000);
        BankAccount a2 = new BankAccount(0,0);
        BankAccount a3 = a2;

        a1.deposit(10);
        a2.deposit(20);
        a3.deposit(30);

        System.out.println("a1:" + a1.balance);
        System.out.println("a2:" + a2.balance);
        System.out.println("a3:" + a3.balance);

    }

}