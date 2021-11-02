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

import pyrebase
from getpass import getpass
import json

firebaseConfig = {

    "apiKey": "AIzaSyDcrStnbgF8af01GqBRIX1GSLr7KZITgT0",
    "authDomain": "vaccinationapp-psp.firebaseapp.com",
    "databaseURL": "https://vaccinationapp-psp-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "vaccinationapp-psp",
    "storageBucket": "vaccinationapp-psp.appspot.com",
    "messagingSenderId": "750323093401",
    "appId": "1:750323093401:web:411b900b196ec9f4910d08",

}

firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()

def authenticate(firebaseConfig, firebase, auth):
    email = input("Please Enter Your Email Address : \n")
    password = getpass("Please Enter Your Password : \n")
    #create users
    #user = auth.create_user_with_email_and_password(email, password)
    #print("Success .... ")
    auth.sign_in_with_email_and_password(email, password)
    #send email verification
    #auth.send_email_verification(login['idToken'])
    #reset the password
    #auth.send_password_reset_email(email)
    print("Login successful")
    return "success"

def editor():
    db = firebase.database()
    while True:
        #action selection    
        firstAction = input('''Please Choose an option:
        1) Create Appointment
        2) Create Vaccination Centre
        3) View Users 
        4) View User Details
                            ''')
        #creates an appointment
        if firstAction == "1" :
            selectedUserId = input("Please input the chosen userId: ")
            selectedCentre = input("Please input the name of the chosen centre: ")
            selectedDate = input("Please input the date [eg: 11-10-2021 ]: ")
            selectedTime = input("Please input the Time [eg: 1:00 PM]: ")
            data = '''{
                        "Accepted" : "Null",
                        "Centre" : "%s",
                        "Date" : "%s",
                        "Time" : "%s"
                    }''' % (selectedCentre, selectedDate, selectedTime)
            db.child("Appointments").child(selectedUserId).set(json.loads(data)) 
            print("Appointment created")
            print(json.loads(data))
        #creates vaccination centre
        elif firstAction == "2" :
            vaccentrename = input("Please input the Centre Name: ")
            vaccentreaddress = input("Please input the Centre Address: ")
            vaccentrepostcode = input("Please input the Centre Post Code: ")
            vaccentrecapacity = input("Please input the Centre Capacity [Vaccination/Hour]: ")
            data = '''{
                        "Address" : "%s",
                        "Capacity" : %s,
                        "PostCode" : "%s",
                        "Slots" : {
                            "10-11-2021" : {
                                "1:00 PM" : {
                                    "Empty" : "Null"
                                },
                                "2:00 PM" : {
                                    "Empty" : "Null"
                                },
                                "3:00 PM" : {
                                    "Empty" : "Null"
                                },
                                "4:00 PM" : {
                                    "Empty" : "Null"
                                }
                            }
                        }
                    }''' % (vaccentreaddress, vaccentrecapacity, vaccentrepostcode)
            db.child("Centres").child(vaccentrename).set(json.loads(data)) 
            print("Centre created")
            print(json.loads(data))
        #views all existing user ID's
        elif firstAction == "3" :
            all_users = db.child("Users").get()
            for user in all_users.each():
                print(user.key())
        #views data of specific user
        elif firstAction == "4" :
            chosenUserId = input("Please input the chosen userId: ")
            print("You chose" + chosenUserId + "here's all corresponding data: ")
            allUserData = db.child("Users").child(chosenUserId).get()
            for item in allUserData.each():
                print(item.key(), item.val())
        #if input number is invalid:
        else:
            print("invalid choice please try again")

while True:
    if authenticate(firebaseConfig, firebase, auth) == "success":
        print(auth.current_user['localId'])
        editor()
    else:
        print("incorrent details")

