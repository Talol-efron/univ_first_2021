import java.util.ArrayList;

abstract class Character {
    private String name;
    private int hp;
    private int mp;
    private int attack;

    /*String name;
    int hp;
    int mp;
    int attack;*/

    ArrayList<Action> actions = new ArrayList<>();

    Character(String name, int hp, int mp, int attack) {
        this.name = name;
        this.hp = hp;
        this.mp = mp;
        this.attack = attack;
    }

    public String getName(){
        return this.name;
    }

    public int getHp(){
        return this.hp;
    }

    public int getMp(){
        return this.mp;
    }

    public int getAttack(){
        return this.attack;
    }

    void damage(int value) {
        hp -= value;
    }

    public void heal(int value) {
        hp += value;
    }

    void comsume(int value) {
        mp -= value;
    }

    void addAction(Action action) {
        actions.add(action);
    }

    public ArrayList<Action> getActions() {
        return actions;
    }

    void showStatus() {
        System.out.printf("%s:HP %d  MP %d\n", name, hp, mp);
    }

    abstract void act(ArrayList<Character> targets); // サブクラスで定義する

	//public void heel(int value) {
	//}
}
