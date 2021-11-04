class HealingGoods extends Goods {
    private int value;

    HealingGoods(String name, int value) {
        // スーパークラスのコンストラクタが引数を要求するので，渡す
        super(name);
        this.value = value;
    }

    // 実際に起きることを記述する
    @Override
    protected void executeImpl(Character executer, Character target) {
        System.out.println(executer.getName() + "は" + name() + "をつかった！");
        target.heal(value);
        System.out.println(target.getName() + "は" + value + "ポイントかいふくした！");
    }
}
