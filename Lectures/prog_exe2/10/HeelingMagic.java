public class HeelingMagic implements Action{
    // 魔法は個別の名前を持つ
    private String name;
    private int heel; // 回復力
    private int consumption; // 消費MP


    HeelingMagic(String name, int heel, int consumption){
        this.name = name;
        this.heel = heel;
        this.consumption = consumption;
    }

    @Override
    public String name(){
        return name;
    }


    @Override
    public void execute(Character executer, Character target) {
        System.out.println(executer.getName() + "は" + name + "をとなえた!!");
        if ( 100 > executer.getHp()){
            executer.comsume(executer.getMp());
            if (100 >= (heel + executer.getHp())){
                executer.heal(heel);
                System.out.println(executer.getName() + "は自身を" + heel + "回復した!!");
            }else{
                /*executer.getHp()= 100;
                System.out.println(executer.getName() + "は体力が満タンになった！！"); */
                
            }

        }else{
            System.out.println("miss!!" + executer.getName() + "はすでに体力満タンんだ");
        }
    }
}