import java.util.ArrayList;
import java.util.Scanner;

class Player extends Character {
    private Equipment weapon; // 装備中の装備品を保持

    Player(String name, int hp, int mp, int attack) {
        super(name, hp, mp, attack);
    }

    private ArrayList<Baggage> baggages = new ArrayList<>(); // 所持品リスト

    // 道具もアクションの一種として選択できるようにオーバーライド
    @Override
    public ArrayList<Action> getActions() {
        // 本来のアクションリストのコピーを生成する
        var integrated_actions = new ArrayList<Action>(super.getActions());

        // 全持ち物を調べる
        for (var b : baggages) {
            // この持ち物は道具か? actionを継承するインスタンスを取り出す．
            if (b instanceof Action) { // instanceofはインスタンスのクラスを調べる
                Action goods = (Action) b;// bはActionのインスタンスであることが
                                          // わかっているので安全にダウンキャストできる
                integrated_actions.add(goods);
            }
        }
        // 統合した一時的なアクションリストを返す
        return integrated_actions;
    }

    // 所持品を追加する
    public void addBaggage(Baggage baggage) {
        baggages.add(baggage);
    }

    @Override
    public int getAttack() {
        // Optionalが使えるならその方がスマートかも
        if (weapon == null) { // 武器を持っていなければ影響なし
            return super.getAttack();
        } else {
            return super.getAttack() + weapon.getAttack();
        }
    }

    // 武器を装備する
    public void equipWeapon(Equipment weapon) {
        this.weapon = weapon;
    }

    @Override
    void act(ArrayList<Character> targets) {
        System.out.println("コマンド？");
        int index = 0;
        for (var action : actions) { // 選択可能なアクションを提示
            System.out.println(index + ":" + action.name());
            index += 1;
        }

        // 標準入力から数値を入力するコード
        Scanner scanner = new Scanner(System.in);
        int command_number = scanner.nextInt();
        

        index = 0;
        System.out.println("ターゲット？");
        for (var ch : targets) { // 選択可能なターゲットを提示
            System.out.println(index + ":" + ch.getName());
            index += 1;
        }

        // 標準入力から数値を入力
        int target_index = scanner.nextInt();

        // 本当は範囲チェックする必要あり
        getActions().get(command_number).execute(this, targets.get(target_index));
        // ^ユーザが選択したアクション番号 ^選択したターゲット番号
    }

}
