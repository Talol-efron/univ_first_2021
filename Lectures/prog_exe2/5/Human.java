class people{
    private int height;
    private int weight;
    private int study;
    private int game;
    private int sleep;

    people(int h, int w, int st, int g, int sl){
        this.height = h;
        this.weight = w;
        this.study = st;
        this.game = g;
        this.sleep = sl;
    }

    public int knowledge(){
        return this.study * this.sleep;
    }

    public int fight(){
        return this.height * this.weight;
    }

    public int gameSkil(){
        return this.game / this.study;
    }
}





public class Human {
    public static void main(String[] args) {
        people taro = new people(175, 60, 4, 4, 8);

        int k = taro.knowledge();
        int f = taro.fight();
        int g = taro.gameSkil();

        System.out.println("推定学力は" + k + "です");
        System.out.println("推定戦闘力は" + f + "です");
        System.out.println("推定e-sportsスキルは" + g + "です");
    }
}
