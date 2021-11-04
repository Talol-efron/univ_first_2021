class Pair{
    int x;
    int y;

    int add(){
    return this.x + this.y;
    }
}
public class PairValue {
    public static void main(String[] args) {
        Pair a = new Pair();
        a.x = 3;
        a.y = 5;
        System.out.println(a.add());
    }
}
