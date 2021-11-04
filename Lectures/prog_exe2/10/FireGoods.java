class FireGoods extends Goods{
    private int value;

    FireGoods(String name, int value){
        // スーパークラスのコンストラクタが引数を要求するので，渡す
        super(name);
        this.value = value;
    }

    @Override
    protected void executeImpl(Character executer, Character target) {
        System.out.println(executer.getName() + "は" + name() + "をつかった！");
        target.damage(value);
        System.out.println(target.getName() + "は" + value + "ポイントの大ダメージを受けた！");
    }
}
