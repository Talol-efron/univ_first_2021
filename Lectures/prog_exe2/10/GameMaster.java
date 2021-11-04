import java.util.ArrayList;

class GameMaster {
    ArrayList<Character> order = new ArrayList<>();
	
    GameMaster() {
        var denchu = new Player("デンチウ", 100, 20, 20);
        // GameMasterクラスのコンストラクタに以下を挿入

        /*var konbo = new Equipment("こんぼう", 15);
        denchu.equipWeapon(konbo);
        denchu.addBaggage(konbo);*/

        // 装備品がbattに上書きされた(実装部分)
        var batt = new Equipment("バット", 20);
        denchu.equipWeapon(batt);
        denchu.addBaggage(batt);
        
        var denchi = new HealingGoods("かんでんち", 30);
        denchu.addBaggage(denchi);

        //実装部分
        var strong = new FireGoods("10万ボルト", 30);
        denchu.addBaggage(strong);
        
        denchu.addAction(new Attack());
        // インスタンスのパラメータを変えることで攻撃魔法のバリエーションを作る
        denchu.addAction(new AttackMagic("ジューデン", 30, 10));
        denchu.addAction(new AttackMagic("ベジュデマ", 60, 20));
        denchu.addAction(new HeelingMagic("ヒーリンング", 50, 20));
    

        var dan = new Enemy("ダンさん", 40, 10, 10);
        dan.addAction(new Attack());
        // アクションの順序を決める
        order.add(denchu);
        order.add(dan);
        
    }

    void showStatus() { // 全キャラクタのステータスを表示（テスト用）
        for (var ch : order) {
            ch.showStatus();
        }
    }

    void battle() { // １ターン実行する
        for (var ch : order) {
            ch.act(order);
        }
    }

    boolean playGame() { //敵を倒した際に戦闘終了
        for (var ch : order){
            if(ch.getHp() <= 0){
                System.out.println("戦闘終了");
                return true;
            }
        }
        return false;
    }
}
