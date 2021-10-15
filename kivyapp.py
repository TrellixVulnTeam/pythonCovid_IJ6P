from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import  Button
import requests
import json

class KivyApp(App):
    firebase_url = "https://vaccinationapp-psp-default-rtdb.asia-southeast1.firebasedatabase.app/.json"
    def build(self):
        box_layout = BoxLayout()
        box_layout.orientation = 'vertical'
        button = Button(text="Create Patch")
        button.bind(on_press=self.create_patch)
        button_get = Button(text="Get Data")
        button_get.bind(on_press=self.create_get)
        button_post = Button(text="Post Data")
        button_post.bind(on_press=self.create_post)
        button_put = Button(text="Put Data")
        button_put.bind(on_press=self.create_put)
        button_delete = Button(text="Delete Data")
        button_delete.bind(on_press=self.create_delete)
        button_signout = Button(text="Sign Out")
        button_signout.bind(on_press=self.sign_out)
        box_layout.add_widget(button_get)
        box_layout.add_widget(button_put)
        box_layout.add_widget(button_post)
        box_layout.add_widget(button_delete)
        box_layout.add_widget(button_signout)
        return box_layout

    def create_patch(self, *args):
        print("Buton Clicked")
        json_data = '{"url": "amazon.com", "age": "17"}'
        res = requests.patch(url=self.firebase_url, json=json.loads(json_data))
        print(res.json())

    def create_get(self, *args):
        print("Buton get Clicked")
        res = requests.get(url=self.firebase_url)
        print(res.json())
    
    def create_post(self, *args):
        print("Buton post Clicked")
        json_data = '{"Table1":{"url": "amazon.com", "age": "17"}}'
        res = requests.post(url=self.firebase_url, json=json.loads(json_data))
        print(res.json())
    
    def create_put(self, *args):
        print("Buton put Clicked")
        json_data = '{"Table2":{"url": "google.com", "age": "15"}}'
        res = requests.put(url=self.firebase_url, json=json.loads(json_data))
        print(res.json())
    
    def create_delete(self, *args):
        print("Buton delete Clicked")
        del_url = "https://vaccinationapp-psp-default-rtdb.asia-southeast1.firebasedatabase.app/"
        res = requests.delete(url=del_url+"Table2"+".json")
        print(res.json())

    def sign_out(self):
        self.root.ids.firebase_login_screen.log_out()
        self.root.current = 'firebase_login_screen'

if __name__ == '__main__':
    KivyApp().run()