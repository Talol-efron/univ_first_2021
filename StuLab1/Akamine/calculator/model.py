# -*- coding: utf-8 -*-

class Model:
    def __init__(self, view):  # コンストラクタ
        # インスタンス変数の宣言と初期化
        # これらのインスタン変数は，Calculatorクラスの全てのメソッドで共有される
        # メソッドを抜けても，インスタンスが存在する限り値は保持される
        self.operand = 0      # 演算の対象となる値（被演算子）をオペランドとよぶ
        self.operator = "+"  # 演算子("+","-",など)
        self.result = 0       # 計算結果を保存する
        self.view = view      # viewへの参照. modelの変更を通知する

    def clear(self):
        self.operand = 0
        self.operator = "+"
        self.result = 0
        self.view.showOperand(0)  # viewへ通知

    # 値を入力

    def setValue(self, value):
        self.operand = value
        self.view.showOperand(value)  # viewへ通知

    # 演算子を入力
    def setOperator(self, operator):
        self.operator = operator

    # 演算を実行する
    def calculate(self):
        # 動作確認用print(いわゆるprintデバッグ)
        print("calculate", self.result, self.operator,  self.operand)
        # switchがないので．．．(もっとスマートに書く方法もありますがわかりやすさ優先)

        if self.operator == "+":
            self.result += self.operand
        elif self.operator == "-":
            self.result -= self.operand
        elif self.operator == "*":
            self.result *= self.operand
        elif self.operator == "/":
            self.result /= self.operand
        elif self.operator == "%":
            self.result %= self.operand
        elif self.operator == "^":
            self.result **= self.operand


        self.view.showResult(self.result)  # viewへ通知
