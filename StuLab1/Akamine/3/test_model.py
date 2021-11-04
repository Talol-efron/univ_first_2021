import unittest
from model import Model

# スタブクラス printするとterminalを汚すのでなにもしない


class View:
    def showResult(self, value):
        pass

    def showOperand(self, value):
        pass

# unittest


class ModelTest(unittest.TestCase):
    def setUp(self):
        # このメソッドは，テストごとに事前に実行される
        # setUp() -> testMinus() -> setUp() -> .. のように
        view = View()
        self.model = Model(view)  # modelはviewを参照する

    def testMinus(self):
        # ユーザーが数値を入力
        self.model.setValue(1)

        # ユーザーが演算子キーを押す
        self.model.calculate()  # 演算子キーを押すと計算実行
        self.model.setOperator("-")  # 演算子を保存

        # 演算子キーを初めて押した時は，"+"のはずなので1
        self.assertEqual(self.model.result, 1)

        # ユーザーが数値を入力
        self.model.setValue(2)
        # ユーザーがイコールキーを押す
        self.model.calculate()  # 演算子キーを押すと計算実行
        # イコールキーは演算子ではないので記録しない

        # ここでresultが-1であればOK
        self.assertEqual(self.model.result, -1)

    def testMultiply(self):
        # ユーザーが数値を入力
        self.model.setValue(25)
        self.model.calculate()  # 演算子キーを押すと計算実行
        self.model.setOperator("*")  # 演算子を保存

        self.assertEqual(self.model.result, 25)

        self.model.setValue(4)
        self.model.calculate()  # 演算子キーを押すと計算実行
        self.model.setOperator("+")  # 演算子を保存

        self.assertEqual(self.model.result, 25*4)

        self.model.setValue(50)
        self.model.calculate()  # 演算子キーを押すと計算実行
        self.model.setOperator("-")  # 演算子を保存

        self.assertEqual(self.model.result, 25*4+50)


if __name__ == "__main__":
    unittest.main()
