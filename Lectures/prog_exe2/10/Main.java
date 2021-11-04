public class Main {
    public static void main(String[] args) {
        var master = new GameMaster();

        while(true){
            master.showStatus();
            master.battle();
            
            if(master.playGame()){
                break;
            }
        }
   }
}
