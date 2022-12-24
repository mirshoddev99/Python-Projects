from tkinter import *
from tkinter import messagebox

import requests

API_KEY = "3ba9789e25dd4260c17385f9a3a22a6b"
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


def get_weather(city):
    result = requests.get(url.format(city, API_KEY))

    if result.status_code == 200:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        tem_kelvin = json['main']['temp']
        tem_celsius = tem_kelvin - 273.15
        tem_fahrenheit = (tem_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, tem_celsius, tem_fahrenheit, icon, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_lbl['text'] = '{:.2f}°C , {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]
        icon_ref = PhotoImage(file="weather_icons/{}.png".format(weather[4]))
        image['image'] = icon_ref
        image.image = icon_ref
    else:
        messagebox.showerror('Coudn\'t find.')


app = Tk()
app.title("Weather app")
app.geometry("700x500")

Font_tuple = [("Comic Sans MS", 20, "normal"), ("Times New Roman", 20, "bold"), ("Franklin Gothic Medium Cond", 15, 'italic')]

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search weather", width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text="Location", font=Font_tuple[1], pady=20)
location_lbl.pack()

image = Label(app, image="", pady=15)
image.pack()

temp_lbl = Label(app, text="", pady=10, font=Font_tuple[2])
temp_lbl.pack()

weather_lbl = Label(app, text="", pady=-5, font=Font_tuple[0])
weather_lbl.pack()

app.mainloop()
