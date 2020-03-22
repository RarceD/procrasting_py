import kivy
from kivy.app import App
from kivy.uix.label import Label
print("YES")
class MyApp(App):
    def build(self):
        return Label(text = "This is a test")
if __name__ == "__main__":
    MyApp().run()