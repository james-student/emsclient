import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
##from plyer import gps


class MainScreen(Screen, Widget):
    pass

class messageOrganisersScreen(Screen, Widget):
    msgInput = ObjectProperty(None)
    def sendMsg(self):
        print("Your message was: ", self.msgInput.text)
        self.msgInput.text = ""

class sendLocationScreen(Screen, Widget):
    def sendManualLocation(self):
        print("Your location will be sent.")
    ##def sendLocation(self):
##      gps.configure(on_location=self.on_gps_location)
##      gps.start()
##
##    def on_gps_location(self, **kwargs):
##        kwargs['lat']
##        kwargs['lon']
##        print(kwargs)

class inboxScreen(Screen, Widget):
    pass

class distressScreen(Screen,Widget):
    def sendDistress(self):
        print("Distress signal will be sent")

#Set this class as the screen manager (ability to switch between multiple screens)
class ScreenManagement(ScreenManager, Widget):
    pass



presentation = Builder.load_file("emsclient.kv")


class emsClient(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    emsClient().run()
