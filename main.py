from os import times
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.event import EventDispatcher
from kivy.uix.textinput import TextInput
from kivymd.toast import toast
from kivy.factory import Factory
import requests
import json
import os.path
import time
import sys

sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from json import dumps
import os.path

from covidstatusscreen import CovidStatusScreen
from mainscreen import MainScreen
from profilepagescreen import ProfilePageScreen

folder = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(folder + "/covidstatusscreen.kv")
Builder.load_file(folder + "/mainscreen.kv")
Builder.load_file(folder + "/profilepagescreen.kv")

class MainApp(MDApp, EventDispatcher):

    fireUrl = "https://vaccinationapp-psp-default-rtdb.asia-southeast1.firebasedatabase.app/"
    user_idToken = ""
    local_id = ""

    #displays whatever info
    def display_userInfo(self, userInfo):
       self.root.ids.the_label.text = "local_id: " + self.local_id # + "\n userInfo: " + self.userInfo

    #Loading Screen
    # debug = False
    # popup = Factory.LoadingPopup()
    # popup.background = folder + "/transparent_image.png"
    
    #update covid status
    def update_covid_status(self, covidstatus, occupation, age, medicalcondition, *args):
        priority = ""
        if ( occupation == "Healthcare" or "Community Service"):
            priority = "High"
        elif ( occupation == "Social Service" or "Teaching"):
            priority = "Medium"
        else:
            priority = "Low"

        risk = ""
        if ( medicalcondition == "" or medicalcondition == "N/A"):
            risk = "Low"
        else:
            risk = "High"
        json_data = '''{
                            "Age" : "%s",
                            "Covid-19 stauts" : "%s",
                            "Risk" : "%s",
                            "Medical Conditions" : "%s",
                            "Name" : "Omar Medhat",
                            "Occupation" : "%s",
                            "Priority" : "%s",
                            "Assigned Centre" : "null",
                            "Phone" : "0142345515",
                            "PostCode" : 63000
                        }''' % (age, covidstatus, risk, medicalcondition, occupation, priority)
        print(self.local_id, json_data)
        requests.put(url=self.fireUrl+"/Users/"+self.local_id+".json", json=json.loads(json_data))


    #sign out
    def sign_out(self):
        self.root.ids.firebase_login_screen.log_out()
        self.root.current = 'firebase_login_screen'

    #uses GET to get user info
    # def getInfo(self, *args):
    #     print("Buton get Clicked")
    #     res = requests.get(url=self.fireUrl+"Users/"+self.local_id+".json")
    #     print(res.json())
    #     userInfo = res.json()
    #     return userInfo

    # Creates an empty record for user
    # def initialInfo(self, *args):
    #     print("Initial Record Created")
    #     json_data = {
    #                     "Age" : "null",
    #                     "Covid-19 stauts" : "null",
    #                     "Health Risk" : "null",
    #                     "Medical Conditions" : "null",
    #                     "Name" : "null",
    #                     "Occupation" : "null",
    #                     "Assigned Centre" : "null",
    #                     "Phone" : "null",
    #                     "Postcode" : 0
    #                 }
    #     print(json_data)
    #     res = requests.put(url=self.fireUrl+"/Users"+self.local_id+".json", json=json.loads(json_data))
    #     print(res.json())

    #Updates User Info
    # def updateInfo(self, *args):
    #     print("Buton put Clicked")
    #     json_data = {
    #                     "Age" : "17",
    #                     "Covid-19 stauts" : "normal",
    #                     "Health Risk" : "Low",
    #                     "Medical Conditions" : "null",
    #                     "Name" : "Omar Medhat",
    #                     "Occupation" : "Web dev",
    #                     "Assigned Centre" : "null",
    #                     "Phone" : "0142345515",
    #                     "PostCode" : 63000
    #                 }
    #     print(json_data)
    #     res = requests.put(url=self.fireUrl+"/Users"+self.local_id+".json", json=json.loads(json_data))
    #     print(res.json())
MainApp().run()