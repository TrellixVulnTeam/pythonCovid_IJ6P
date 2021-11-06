# *********************************************************
# Program: main.py [User App], admin.py [Admin App]
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL1V, TL3V, TL4L
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211102907 | Ashlee | 1211102907@student.mmu.edu.my | 019-9700503
# Member_2: 1191101006 | Vetha | 1191101006@student.mmu.edu.my | 012-5775721
# Member_3: 1201103274 | Lai Yin Wei | 1201103274@student.mmu.edu.my | 011-56900813
# Member_4: 1201103094 | Omar Medhat Solieman | 1201103094@student.mmu.edu.my | 014-2345515
# *********************************************************
# Task Distribution
# Member_1: 
# Member_2:
# Member_3:
# Member_4:
# *********************************************************

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
from appointmentscreen import AppointmentScreen

folder = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(folder + "/covidstatusscreen.kv")
Builder.load_file(folder + "/mainscreen.kv")
Builder.load_file(folder + "/profilepagescreen.kv")
Builder.load_file(folder + "/appointmentscreen.kv")

class MainApp(MDApp, EventDispatcher):

    #Credentials
    fireUrl = "https://vaccinationapp-psp-default-rtdb.asia-southeast1.firebasedatabase.app/"
    user_idToken = ""
    local_id = ""

    #displays whatever info
    def display_userInfo(self, userInfo):
       self.root.ids.the_label.text = "local_id: " + self.local_id # + "\n userInfo: " + self.userInfo
    
    #update Profile info
    def update_profile(self, name, age, phonenumber, postcode, occupation, covidstatus, medicalcondition, *args):
        priority = ""
        if ( occupation == "Healthcare" or occupation == "Community Service"):
            priority = "High"
        elif ( occupation == "Social Service" or occupation == "Teaching"):
            priority = "Medium"
        else:
            priority = "Low"

        risk = ""
        if ( medicalcondition == "" or  medicalcondition == "N/A"):
            risk = "Low"
        else:
            risk = "High"

        json_data = '''{
                            "Admin" : "False",
                            "Name" : "%s",
                            "Age" : "%s",
                            "Phone" : "%s",
                            "PostCode" : "%s",
                            "Occupation" : "%s",
                            "Covid-19 status" : "%s",
                            "Medical Conditions" : "%s",
                            "Priority" : "%s",
                            "Risk" : "%s",
                            "Assigned Centre" : "null"
                        }''' % (name, age, phonenumber, postcode, occupation, covidstatus, medicalcondition, priority, risk)
        print(self.local_id, json_data)
        requests.put(url=self.fireUrl+"/Users/"+self.local_id+".json", json=json.loads(json_data))

    #Updates covid status
    def update_covid_status(self, covidstatus, *args):
        print(self.local_id)
        requests.put(url=self.fireUrl+"/Users/"+self.local_id+"/Covid-19 status"+".json", json=covidstatus)

    def display_covid_status(self):
        currentcovidstatus = requests.get(url=self.fireUrl+"/Users/"+self.local_id+"/Covid-19 status"+".json")
        print(currentcovidstatus.json())
        self.root.ids.covid_status_screen.ids.currentstatus.text = "Current Covid-19 status is: " + currentcovidstatus.text


    #sign out
    def sign_out(self):
        self.root.ids.firebase_login_screen.log_out()
        self.root.current = 'firebase_login_screen'

    #Appointment RSVP
    def accept_appt(self):
        requests.put(url=self.fireUrl+"Appointments/"+self.local_id+"/Accepted"+".json", json="True")

    def decline_appt(self):
        requests.put(url=self.fireUrl+"Appointments/"+self.local_id+"/Accepted"+".json", json="False")

    #uses GET to get user info
    def get_assigned(self, *args):
        print("Buton get Clicked")
        centre = requests.get(url=self.fireUrl+"Appointments/"+self.local_id+"/Centre"+".json")
        address = requests.get(url=self.fireUrl+"Centres/"+centre.json()+"/Address"+".json")
        date = requests.get(url=self.fireUrl+"Appointments/"+self.local_id+"/Date"+".json")
        print(centre.json(), date.json(), address.json())
        assignedCentre = centre.json()
        assignedDate = date.json()
        centreaddress = address.json()
        self.root.ids.appointment_screen.ids.assignedcentre.text = "Your Assigned Centre is: " + assignedCentre
        self.root.ids.appointment_screen.ids.centreadress.text = "Your Centre's Address is: " + centreaddress
        self.root.ids.appointment_screen.ids.assigneddate.text = "Your Assigned Date is: " + assignedDate
        return assignedCentre, assignedDate, centreaddress
MainApp().run()