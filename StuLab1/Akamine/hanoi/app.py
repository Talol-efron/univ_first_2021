from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

#他のソースに書いたクラスや関数は以下のようにimportすると呼び出せる
#from ファイル名(.pyは不要) import クラス名, クラス名, ...
from model import Model
from view_controller import View, Controller

Window.size = (600,400)
class HanoiApp(App):
    """ windowやボタンなどUIを構築するクラス．通常OSやフレームワークに強く依存する 
    """
    # display = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        view = View(self)
        model = Model(view)
        self.controller = Controller(model)

    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.display = Label(text="***",font_size=32,size_hint=(1,3))
        layout.add_widget(self.display) 

        button_layout = BoxLayout(orientation="horizontal", size_hint=(1,1))

        for b in "123":
            button_layout.add_widget(Button(text=b, font_size=24*3, on_press=self.onPress))

        layout.add_widget(button_layout)
        
        self.controller.onWindowShowed()
        return layout
    
    def onPress(self, button):
        self.controller.onPress(button.text)

    def setDisplayText(self, text):
        self.display.text = text



if __name__ == "__main__":
    HanoiApp().run()