class status{
    private double hight;
    private double weight;
    private double charge;
    private double electlon;

    status(double h, double w, double c, double e){
        this.hight = h;
        this.weight = w;
        this.charge = c;
        this.electlon = e;
    }
    public double attack(){
        return this.weight * this.charge;
    }

    public double block(){
        return this.electlon * this.hight;
    }
}

public class Dentiu{
    public static void main(String[] args) {
        status denzou = new status(2,1,4,5);
        double p = denzou.attack();
        double b = denzou.block();
        System.out.println("デンゾウの攻撃力は" + p + "です");
        System.out.println("デンゾウの防御力は" + b + "です");
    }
}