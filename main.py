from kivy.app import App
from kivy.uix.button import Button




import android

class TestApp(App):
    def build(self):

        android.start_service(title='testing 1', description='description', arg='')


        return Button(text='Hello World')

if __name__ == '__main__':
    TestApp().run()
