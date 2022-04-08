import tkinter as tk
import requests

root = tk.Tk()
root.config(padx=50, pady=50)

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()

    canvas.itemconfig(canvas_quote, text=f"{quote['quote']}")

canvas = tk.Canvas(width=300, height=414, highlightthickness=0)
bg = tk.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=bg)
canvas_quote = canvas.create_text(150, 207, text="Placeholder", width=250, font=("Arial", 20, "bold"))
canvas.pack()

face = tk.PhotoImage(file="kanye.png")
kanye = tk.Button(image=face, command=get_quote)
kanye.pack()

get_quote()

root.mainloop()
