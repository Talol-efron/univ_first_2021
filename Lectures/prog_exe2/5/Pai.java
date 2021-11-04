class half{
    private double lenght;
    
    half(double l){
        this.lenght = l;
    }
    public double calcPai(){
        return this.lenght * this.lenght * Math.PI;
    }

    public double calcArea(){
        return (this.lenght + this.lenght) * Math.PI;
    }
}

public class Pai {
    public static void main(String[] args) {
        half h = new half(1);
        double p = h.calcPai();
        double q = h.calcArea();
        System.out.println("円周は" + p + "です");
        System.out.println("円の面積は" + q + "です");
    }
}
