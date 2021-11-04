from model import Model

#スタブクラス 単にprintするだけ


class View:
    def showResult(self, value):
        print("result:", value)

    def showOperand(self, value):
        print("operand:", value)

#ドライバークラス


class Controller:
    def __init__(self, model):
        self.model = model  # 操作対象のモデル

    def run_test(self):
        #このシーケンスについては，詳細設計を参照

        #ユーザーが数値を入力
        self.model.setValue(1)
        #ユーザーが演算子キーを押す
        self.model.calculate()  # 演算子キーを押すと計算実行
        self.model.setOperator("-")  # 演算子を保存

        #ユーザーが数値を入力
        self.model.setValue(2)
        #ユーザーがイコールキーを押す
        self.model.calculate()  # 演算子キーを押すと計算実行
        #イコールキーは演算子ではないので記録しない


if __name__ == "__main__":
    view = View()
    model = Model(view)  # modelはviewを参照する
    controller = Controller(model)  # controllerはmodelを参照する

    controller.run_test()
