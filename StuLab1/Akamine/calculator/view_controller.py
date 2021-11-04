

class InvalidInput(Exception):
    """ 入力関連のエラー """
    pass

class View:
    def __init__(self, ui_framework):
        self.uiFramework = ui_framework

    def showResult(self, value):
        self.uiFramework.setDisplayText(str(value))

    def showOperand(self, value): #displayは一つなので共用
        self.uiFramework.setDisplayText(str(value))

class Controller:
    def __init__(self, model):
        #オブジェクト間で情報をやりとりするには，データの通知先オブジェクトのインスタンスが参照可能である必要がある
        self.model = model #モデルへアクセスするためオブジェクトの参照をもつ
        self.inputNumber = 0 #入力中の数

    def onPress(self, key): #キーが押された時の処理
        if key.isdigit():
            self.inputNumber = self.inputNumber * 10 + int(key)
            self.model.setValue(self.inputNumber)
        elif key in "+-/*^%": #演算子キーか？
            # 演算キーが押された時，演算を行う
            self.model.calculate()
            self.model.setOperator(key)
            # 入力中の値はクリア
            self.inputNumber = 0
        elif key == "=":
            self.model.calculate()
            self.inputNumber = 0
        elif key == "C":
            self.model.clear()
            self.inputNumber = 0
        elif key == " ":
            pass
        else:
            #上記条件に当てはまらないkeyは誤り
            raise InvalidInput('定義されていないキー')

