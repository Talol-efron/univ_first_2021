class AttackGoods extends Goods {
    private int value;

    AttackGoods(String name, int value) {
        // スーパークラスのコンストラクタが引数を要求するので，渡す
        super(name);
        this.value = value;
    }

    // 実際に起きることを記述する
    @Override
    protected void executeImpl(Character executer, Character target) {
        System.out.println(executer.getName() + "は" + name() + "をつかった！");
        target.damage(value);
        System.out.println(executer.getName() + "は" + target.getName() + "に" + value + "ポイントのダメージを与えた!");
    }
}
