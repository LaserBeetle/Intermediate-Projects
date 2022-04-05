import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/japanese_words.csv")

to_learn = data.to_dict(orient="records")
new_word = {}


def next_card():
    global new_word, flip_timer
    root.after_cancel(flip_timer)
    new_word = random.choice(to_learn)
    card.itemconfig(canvas_image, image=front_img)

    if len(new_word["Japanese"]) < 25:
        card.itemconfig(title, text="Japanese", fill="black", font=("Ariel", 50, "italic"))
        card.itemconfig(old_word, text=new_word["Japanese"], fill="black", font=("Ariel", 30, "bold"))
    else:
        card.itemconfig(title, text="Japanese", font=("Ariel", 50, "italic"))
        card.itemconfig(old_word, text=new_word["Japanese"], font=("Ariel", 15, "bold"))

    flip_timer = root.after(3000, flip_card)


def flip_card():
    card.itemconfig(canvas_image, image=back_img)
    card.itemconfig(title, text="English", fill="white", font=("Ariel", 50, "italic"))
    card.itemconfig(old_word, text=new_word["English"], fill="white", font=("Ariel", 30, "bold"))


def remove_card():
    to_learn.remove(new_word)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    next_card()


root = tkinter.Tk()
root.title("FlashCards")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = tkinter.PhotoImage(file="images/card_front.png")
back_img = tkinter.PhotoImage(file="images/card_back.png")
canvas_image = card.create_image(400, 263, image=front_img)
title = card.create_text(400, 150, text="Placeholder", fill="black", font=("Ariel", 50, "italic"))
old_word = card.create_text(400, 300, text="Placeholder", fill="black", font=("Ariel", 30, "bold"))
card.grid(column=0, row=0, columnspan=2)

wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_img, highlightthickness=0, command=remove_card)
right_button.grid(column=1, row=1)

flip_timer = root.after(3000, flip_card)
next_card()
root.mainloop()
