import unittest
from model import Model

WIN = 0
LOSE = 1
TIE = 2

# スタブクラス 結果を得るために使う


class View:
    def __init__(self):
        self.hand = 0
        self.result = ""

    def showHand(self, hand_id):
        self.hand = hand_id

    def win(self):
        self.result = WIN

    def lose(self):
        self.result = LOSE

    def tie(self):
        self.result = TIE


GU = 0
CHOKI = 1
PA = 2


class ModelTest(unittest.TestCase):

    def setUp(self):
        # このメソッドは，テストごとに事前に実行される
        # setUp() -> testMinus() -> setUp() -> .. のように
        self.view = View()
        self.model = Model(self.view)  # modelはviewを参照する

    def testGu(self):  # グーを出した時のテスト
        for _ in range(100):
            self.model.pon(GU)

            if self.view.hand == GU:
                self.assertTrue(self.view.result == TIE)
            elif self.view.hand == CHOKI:
                self.assertTrue(self.view.result == WIN)
            else:
                self.assertTrue(self.view.result == LOSE)

    def testChoki(self):  # チョキを出した時のテスト
        for _ in range(100):
            self.model.pon(CHOKI)

            if self.view.hand == CHOKI:
                self.assertTrue(self.view.result == TIE)
            elif self.view.hand == PA:
                self.assertTrue(self.view.result == WIN)
            else:
                self.assertTrue(self.view.result == LOSE)

    def testPa(self):  # パーを出した時のテスト
        for _ in range(100):
            self.model.pon(PA)

            if self.view.hand == PA:
                self.assertTrue(self.view.result == TIE)
            elif self.view.hand == GU:
                self.assertTrue(self.view.result == WIN)
            else:
                self.assertTrue(self.view.result == LOSE)


if __name__ == "__main__":
    unittest.main()
