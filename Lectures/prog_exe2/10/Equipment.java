class Equipment implements Baggage {
    private int attack;
    private String name;

    Equipment(String name, int attack) {
        this.attack = attack;
        this.name = name;
    }

    int getAttack() {
        return attack;
    }

    @Override
    public String name() {
        return name;
    }
}
