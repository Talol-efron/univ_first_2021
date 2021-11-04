HANDS = ["gu", "choki", "pa"]


class View:
    def __init__(self, ui_framework):
        self.uiFramework = ui_framework

    def showHand(self, hand_id):
        self.uiFramework.setHand(HANDS[hand_id])

    def win(self):
        self.uiFramework.setText("You win!")

    def lose(self):
        self.uiFramework.setText("You lose!")

    def tie(self):
        self.uiFramework.setText("Ai ko desho!")


class Controller:
    def __init__(self, model):
        # オブジェクト間で情報をやりとりするには，
        # データの通知先オブジェクトのインスタンスが参照可能である必要がある
        self.model = model  # モデルへアクセスするためオブジェクトの参照をもつ

    def onPress(self, button):  # ボタンが押された時の処理
        hand_id = HANDS.index(button)
        self.model.pon(hand_id)  # 型(グーチョキパー)のid(0-2)を返す
        # 0: グー, 1:チョキ, 2:パー
