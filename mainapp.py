from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import ThreeLineAvatarListItem

import requests



class ItemWeather(ThreeLineAvatarListItem):
    source = StringProperty('string')


class ContentNavigationDrawer(BoxLayout):
    pass


class HomeScreen(Screen):
    pass


class AboutScreen(Screen):
    pass



class MainWidget(BoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        return MainWidget()

    def on_start(self):
        bbox = '12,32,15,37,10'
        home_list = self.root.ids.home_list
        response = requests.get('https://api.openweathermap.org/data/2.5/box/city?bbox='+bbox+'&appid=423b9f143277a4e67efc66ffdf211c37')
        #response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=43.9&lon=-73.9'+'&appid=423b9f143277a4e67efc66ffdf211c37')
        jsonResponse = response.json()
        weather_list = jsonResponse['list']

        for item in weather_list:
            name = item['name']
            temp = str(item['main']['temp'])
            humidity = str(item['main']['humidity'])
            description = item['weather'][0]['description']

            image = ''

            if description == 'clear sky':
                image = 'data/01d.png'
            elif description == 'few clouds':
                image = 'data/02d.png'
            elif description == 'scattered clouds':
                image = 'data/03d.png'
            elif description == 'broken clouds':
                image = 'data/04d.png'
            elif description == 'shower rain':
                image = 'data/09d.png'
            elif description == 'rain': 
                image = 'data/10d.png'
            elif description == 'thunderstorm':
                image = 'data/11d.png'
            elif description == 'snow':
                image = 'data/13d.png'
            elif description == 'mist':
                image = 'data/50d.png'
            else:      
                image = 'data/01d.png'                             



            item = ItemWeather(text=name, secondary_text='Nhiệt độ: '+ temp +' - Độ ẩm: '+ humidity, tertiary_text=description, source=image)
            home_list.add_widget(item)


        about_label = self.root.ids.about_label
        about_label.text = "This is my awesome app"    



        


MainApp().run()