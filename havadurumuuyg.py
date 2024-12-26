import requests
import tkinter as tk
from tkinter import messagebox


API_KEY = 'f5ccbe8cf676cc8c2fb8ebf6c9457d80'  
url = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city_name):
    try:
        # API isteği
        params = {'q': city_name + ',TR', 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(url, params=params)
        data = response.json()

        if data['cod'] == 200: 
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            description = data['weather'][0]['description']

            result = f"Şehir: {city}, {country}\n"
            result += f"Sıcaklık: {temp}°C\n"
            result += f"Nem: {humidity}%\n"
            result += f"Rüzgar Hızı: {wind_speed} m/s\n"
            result += f"Açıklama: {description}"
        else:
            result = "Şehir bulunamadı."
        
        return result
    except Exception as e:
        return "Hava durumu bilgisi alınırken bir hata oluştu."


def show_weather():
    city_name = city_entry.get()
    if city_name:
        weather_info = get_weather(city_name)
        result_label.config(text=weather_info)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin.")

# Tkinter GUI
root = tk.Tk()
root.title("Hava Durumu Uygulaması")

# Şehir girme alanı
city_label = tk.Label(root, text="Şehir Adı:")
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

# Hava durumu gösterme butonu
search_button = tk.Button(root, text="Hava Durumunu Göster", command=show_weather)
search_button.pack(pady=10)

# Hava durumu bilgisi gösterme alanı
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
