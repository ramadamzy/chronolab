import tkinter as tk
from tijdreizen import reis_naar_1886, reis_naar_1969, reis_naar_2026

def start_1886():
    reis_naar_1886()

def start_1969():
    reis_naar_1969()

def start_2026():
    reis_naar_2026()

window = tk.Tk()
window.title("ChronoLab - Tijdreis Game")
window.geometry("400x300")

label = tk.Label(window, text="Kies je tijdperk", font=("Arial", 16))
label.pack(pady=20)

btn1 = tk.Button(window, text="1886", command=start_1886)
btn1.pack(pady=5)

btn2 = tk.Button(window, text="1969", command=start_1969)
btn2.pack(pady=5)

btn3 = tk.Button(window, text="2026", command=start_2026)
btn3.pack(pady=5)

window.mainloop()
