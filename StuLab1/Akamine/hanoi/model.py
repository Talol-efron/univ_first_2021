# -*- coding: utf-8 -*-
import random

class Model:
    def __init__(self, view):  # コンストラクタ
        # インスタンス変数の宣言と初期化
        # これらのインスタン変数は，Calculatorクラスの全てのメソッドで共有される
        # メソッドを抜けても，インスタンスが存在する限り値は保持される
        self.view = view      # viewへの参照. modelの変更を通知する
        self.selection = [0]*2
        self.selection_index = 0

    def start(self):
        self.view.display("Which disk do you want to move?")


    def select(self, num):
        self.selection[self.selection_index] = num

        #text = "please show hanoi disk here\n"
        text = ""
        if self.selection_index == 0:
            text += "Where do you want to move a disk from %d?\n" % self.selection[0]
        else:
            text += "move %d to %d\n" % tuple(self.selection)
            text += "Which disk do you want to move?"

        self.selection_index = 1 - self.selection_index
        self.view.display(text)

