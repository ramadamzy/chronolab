import tkinter as tk
from tijdreizen import reis_naar_1886, reis_naar_1969, reis_naar_2026

score = 0
current_answer = ""
correct_answer = ""

def set_question(question, answer):
    global correct_answer, current_answer
    correct_answer = answer
    current_answer = ""

    question_label.config(text=question)
    entry.delete(0, tk.END)
    status.config(text="")

def check_answer():
    global score

    answer = entry.get().strip().lower()

    if answer == correct_answer:
        score += 1
        status.config(text=f"✔ Goed! Score: {score}", fg="#00ff88")
    else:
        status.config(text=f"✖ Fout! Score: {score}", fg="#ff4d4d")


# Tijdreizen functies (zelfde vragen als jouw code)

def start_1886():
    set_question("Wat is 12 + 8?", "20")

def start_1969():
    set_question("Welke planeet staat bekend als de Rode Planeet?", "mars")

def start_2026():
    set_question("Welk woord verbindt computers met elkaar?", "netwerk")


# WINDOW
window = tk.Tk()
window.title("CHRONOLAB")
window.geometry("600x450")
window.configure(bg="#0b0f1a")

title = tk.Label(
    window,
    text="CHRONOLAB",
    font=("Arial", 28, "bold"),
    fg="#00e5ff",
    bg="#0b0f1a"
)
title.pack(pady=10)

subtitle = tk.Label(
    window,
    text="Los puzzels op en herstel de tijdlijn",
    font=("Arial", 11),
    fg="#aab4c4",
    bg="#0b0f1a"
)
subtitle.pack(pady=5)

# BUTTONS
def make_button(text, command, color):
    return tk.Button(
        window,
        text=text,
        command=command,
        font=("Arial", 12, "bold"),
        fg="white",
        bg=color,
        activebackground="#1a1f2b",
        width=30,
        bd=0,
        pady=8
    )

btn1 = make_button("🕰️ Reis naar 1886", start_1886, "#1f6feb")
btn1.pack(pady=5)

btn2 = make_button("🚀 Reis naar 1969", start_1969, "#9b59b6")
btn2.pack(pady=5)

btn3 = make_button("💻 Reis naar 2026", start_2026, "#00b894")
btn3.pack(pady=5)


# QUESTION DISPLAY
question_label = tk.Label(
    window,
    text="Kies een tijdperk",
    font=("Arial", 12),
    fg="white",
    bg="#0b0f1a"
)
question_label.pack(pady=15)

# INPUT FIELD
entry = tk.Entry(window, font=("Arial", 12), width=30)
entry.pack(pady=5)

# CHECK BUTTON
check_btn = tk.Button(
    window,
    text="Antwoord controleren",
    command=check_answer,
    font=("Arial", 12, "bold"),
    fg="black",
    bg="#00e5ff",
    width=25
)
check_btn.pack(pady=10)

# STATUS
status = tk.Label(
    window,
    text="Score: 0",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#0b0f1a"
)
status.pack(pady=20)

window.mainloop()
