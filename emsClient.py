# Imports
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


# Main screen - pass in screen and widget module from Kivy
class MainScreen(Screen, Widget):
    pass

# Message organisers screen - pass in screen and widget module from Kivy
    # Take input from user and set as msgInput
    msgInput = ObjectProperty(None)
    # Function for sending message

    def sendMsg(self):
        # For development: print message to screen
        print("Your message was: ", self.msgInput.text)
        self.msgInput.text = ""

# Send location screen - pass in screen and widget module from Kivy


class sendLocationScreen(Screen, Widget):
    # Function to send location
    def sendManualLocation(self):
        # For development: print a generic message to screen
        print("Your location will be sent.")

# Inbox screen


class inboxScreen(Screen, Widget):
    pass

# Distress signal screen


class distressScreen(Screen, Widget):
    # Class for sending a distress signal
    def sendDistress(self):
        # For development: print a generic message to screen
        print("Distress signal will be sent")

# Set this class as the screen manager (ability to switch between multiple screens)


class ScreenManagement(ScreenManager, Widget):
    pass


# Load emsclient.kv as styling file
presentation = Builder.load_file("emsclient.kv")


# Build the app
class emsClient(App):
    def build(self):
        return presentation


# Run the app
if __name__ == "__main__":
    emsClient().run()
