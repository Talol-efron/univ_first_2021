import java.util.ArrayList;

class Enemy extends Character {
    Enemy(String name, int hp, int mp, int attack) {
        super(name, hp, mp, attack);
    }

    @Override
    void act(ArrayList<Character> targets) {
        // テスト用コード
        // targets.get(0)はデンチウのはず．．．
        actions.get(0).execute(this, targets.get(0));
    }
}
