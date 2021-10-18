import json
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.factory import Factory
import time
import requests

class CovidStatusScreen(Screen, EventDispatcher):
    fireUrl = "https://vaccinationapp-psp-default-rtdb.asia-southeast1.firebasedatabase.app/"
    user_idToken = ""
    local_id = ""

    def go_back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = self.parent.current = "main_screen"
        self.parent.transition = SlideTransition(direction="left")