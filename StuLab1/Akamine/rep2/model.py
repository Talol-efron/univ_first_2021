# -*- coding: utf-8 -*-
import random

class Model:
    def __init__(self, view):  # コンストラクタ
        # インスタンス変数の宣言と初期化
        # これらのインスタンス変数は，Calculatorクラスの全てのメソッドで共有される
        # メソッドを抜けても，インスタンスが存在する限り値は保持される
        self.view = view      # viewへの参照. modelの変更を通知する

    def getComputersHand(self):
        return random.randint(0, 2)  # 0以上２以下の乱数を返す

    def pon(self, uhand_id):
        chand_id = self.getComputersHand()
        # 0:グー, 1:チョキ, 2:パー
        # chandには，コンピュータの手を表す0-2のいずれかの数（乱数）が保存されている．
        #ユーザが選択した手は, uhand_idに代入されている
        # これを利用して，勝敗引き分けの判定を行い，viewに通知する
        # 通知可能なメソッドは以下の通り
        #           self.view.win()  #ユーザの勝ち
        #           self.view.tie()  #引き分け
        #           self.view.lose() #ユーザの負け

        self.view.showHand(chand_id)
        
        if chand_id == uhand_id:
            self.view.tie()
        elif (chand_id == 0 and uhand_id == 2) or (chand_id == 1 and uhand_id == 0) or (chand_id == 2 and uhand_id == 1):
            self.view.win()
        else:
            self.view.lose()
        
