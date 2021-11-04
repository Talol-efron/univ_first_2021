class NomalPlayer {
    public void invoke(String name) {
        System.out.println(name + "は攻撃した！");
    }
}

class MagicPlayer extends NomalPlayer {
    @Override
    public void invoke(String name) {
        System.out.println(name +"は魔法攻撃をした！");
    }
}

class SkillPlayer extends NomalPlayer {
    @Override
    public void invoke(String name) {
        System.out.println(name + "は木の棒で攻撃をした！");
    }
}

public class Player {
    public static void main(String[] args) {
       NomalPlayer unko = new NomalPlayer();
       unko.invoke("普通の戦士");
       MagicPlayer a = new MagicPlayer();
       a.invoke("魔法使い");
       SkillPlayer s = new SkillPlayer();
       s.invoke("勇敢な戦士");
    }
}
