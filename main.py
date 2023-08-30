from PIL import ImageTk, Image
import tkinter as tk
import requests
import os


m = tk.Tk();

m.title('Python Weather App!')


out = tk.Canvas(m, width = 500, height = 250)
out.pack()


frames = ImageTk.PhotoImage(Image.open("bkg.jpg"))
background_label = tk.Label(m, image=frames)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



l1 = tk.Label(m, text = 'Python Weather Checker')
l1.config(font = ('Times New Roman', 12))
out.create_window(100,25, window = l1)

l2 = tk.Label(m, text = "Enter a city")
l2.config(font = ("Times New Roman", 12))
out.create_window(250,75, window = l2)

textBox = tk.Entry(m, width = 50)
out.create_window(250,100, window = textBox)


def weatherCheck():
    api_key = '2c4af5d54fb76d475486a11dd3907bd4'

    x = textBox.get()

    url = f'http://api.openweathermap.org/data/2.5/weather?q={x}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']

        l3 = tk.Label(m, text = (f'Temperature: {1.8 * (temp - 273) + 32:.2f} F'))
        l3.config(font = ("Times New Roman", 12))
        out.create_window(200,150, window = l3)
        
        l4 = tk.Label(m, text = (f'Description: {desc}'))
        l4.config(font = ("Times New Roman", 10))
        out.create_window(200,200, window = l4)



    else:
        l5 = tk.Label(m, text = ('Error fetching weather data'))
        l5.config(font = ("Times New Roman", 12))
        out.create_window(150,150, window = l5)




button = tk.Button(m, text = 'Submit', width = 10, command = weatherCheck)
button.place(x=1150,y=85)




m.mainloop()

