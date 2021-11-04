class Calculate{
    private double lenght;
    private double width;

    Calculate(double l, double w){
        this.lenght = l;
        this.width = w;
    }

    public double calcArea(){
        return this.lenght * this.width;
    }
}



public class Calculation{
    public static void main(String[] args) {
        Calculate c = new Calculate(4, 5);
        double area = c.calcArea();
        System.out.println("このareaは" + area + "です");
    }
}