//ActionをBaggageを多重継承している
//したがって，GoodsのインスタンスはActionとして実行することも所持することもできる
abstract class Goods implements Action, Baggage {
    int usageCount;
    private String name;

    // コンストラクタの引数として名前を受け取る
    // これによりサブクラスがnameを設定することを強制する
    Goods(String name) {
        this.name = name;
        usageCount = 1;
    } // とりあえず使用回数は1とする

    @Override
    public void execute(Character executer, Character target) {
        // 使用可能か？
        if (usageCount > 0) {
            executeImpl(executer, target);
            usageCount -= 1;
        } else {
            System.out.println("なにもおきなかった．．．");
        }
    }

    @Override
    public String name() {
        if (usageCount == 0) {
            return "使用済みの" + name;
        } else {
            return name;
        }
    }

    // 何が起きるかはサブクラスに任せる
    abstract protected void executeImpl(Character executer, Character target);
    /*
     * Strategyパターンを用いても同様の実装が可能．他のアクションと実装を共有するなど，より 柔軟なコーディングが可能
     */
}
