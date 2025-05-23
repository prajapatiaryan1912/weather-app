import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# Replace with your weatherstack API key
API_KEY = "941edba414ab78c0083cbdb96e84ad55"

# Setup main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.configure(bg="#e6f0ff")

# Title
title_label = tk.Label(root, text="🌦️ Weather App", font=("Helvetica", 20, "bold"), bg="#e6f0ff", fg="#004080")
title_label.pack(pady=10)

# City Entry
city_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
city_entry.pack(pady=10)
city_entry.focus()

city_entry.bind("<Return>",lambda event: get_weather())

# Label to show weather results
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left", bg="#e6f0ff", fg="#004080", wraplength=380)
result_label.pack(pady=10)

# Fetch weather function
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", data["error"]["info"])
            result_label.config(text="Unable to fetch weather data.", fg="red")
            return

        location = data["location"]
        current = data["current"]

        result_text = (
            f"📍      City                    : {location['name']}, {location['country']}\n"
            f"🌡️ Temperature    : {current['temperature']}°C\n"
            f"☁️    Description      : {current['weather_descriptions'][0]}|\n"
            f"💧      Humidity           : {current['humidity']}%\n"
            f"💨    Wind Speed     : {current['wind_speed']} km/h\n"
            f"🕒    updated            : {datetime.now().strftime('%A, %d %B %Y %I:%M %p')}\n"
        )

        result_label.config(text=result_text, fg="#004080")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# Button to get weather
get_weather_btn = tk.Button(root, text="Get Weather", font=("Helvetica", 14), bg="#004080", fg="white", command=get_weather)
get_weather_btn.pack(pady=10)

root.mainloop()
