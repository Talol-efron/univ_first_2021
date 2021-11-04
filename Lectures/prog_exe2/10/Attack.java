class Attack implements Action {
    @Override
    public String name() {
        return "たたかう"; // このアクションの名称（ユーザーに提示される）
    }

    @Override
    /**
     * 実際に実行されるアクションの処理．本クラスでは武器で攻撃
     * 
     * @param executer アクションを実行するキャラクタのインスタンスが入っている
     * @param target   アクションの実行対象（攻撃対象)が入っている
     */
    public void execute(Character executer, Character target) {
        target.damage(executer.getAttack());
        System.out.println(executer.getName() + "の攻撃!!");
        waitMoment(500);
        System.out.println(executer.getName() + "は" + target.getName() + "に" + executer.getAttack() + "ポイントのダメージを与えた!");
        waitMoment(1000);

    }

    // 少し待つ
    public void waitMoment(int time) {
        try {
            Thread.sleep(time);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}
