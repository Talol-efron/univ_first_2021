class Human{
  public void greet(){
    System.out.println("Hi !!");
  }
}

class JapaneseHuman extends Human{
  @Override
  public void greet(){
    System.out.println("こんにちは");
  }
}

class ChineseHuman extends Human{
  @Override
  public void greet(){
    System.out.println("你好");
  }
}

class KorianHuman extends Human {
  @Override
  public void greet() {
    System.out.println("안녕하세요");
  }
}

class Main {
    public static void main(String[] args) {
      JapaneseHuman Taro = new JapaneseHuman();
      ChineseHuman Ri = new ChineseHuman();
      KorianHuman Paku = new KorianHuman();

      Taro.greet();
      Ri.greet();
      Paku.greet();
    }
}
