

class View:
    def __init__(self, ui_framework):
        self.uiFramework = ui_framework

    def display(self, text):
        self.uiFramework.setDisplayText(str(text))

class Controller:
    def __init__(self, model):
        #オブジェクト間で情報をやりとりするには，データの通知先オブジェクトのインスタンスが参照可能である必要がある
        self.model = model #モデルへアクセスするためオブジェクトの参照をもつ

    def onWindowShowed(self):
        self.model.start()

    def onPress(self, button): #キーが押された時の処理
        self.model.select(int(button))

