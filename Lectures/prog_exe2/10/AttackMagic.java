class AttackMagic implements Action {
    // 魔法は個別の名前を持つ
    private String name;
    private int attack; // 攻撃力
    private int consumption; // 消費MP

    AttackMagic(String name, int attack, int consumption) {
        this.name = name;
        this.attack = attack;
        this.consumption = consumption;
    }

    @Override
    public String name() {
        return name;
    }

    @Override
    public void execute(Character executer, Character target) {
        System.out.println(executer.getName() + "は" + name + "をとなえた!!");
        target.damage(executer.getAttack());
        executer.comsume(executer.getMp());
        //executer.mp -= consumption;
        System.out.println(target.getName() + "に" + attack + "ポイントのダメージをあたえた!!");
    }
}

