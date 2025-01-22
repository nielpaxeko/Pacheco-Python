# This Capstone Project is a flascard application for studying French vocabulary using Tkinter
from tkinter import *
from numpy import flip
import pandas as pd
import time
import random as rand
BACKGROUND_COLOR = "#B1DDC6"
current_word = ""
to_learn = {}
# Read data file
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Change Slides
def change_card():
    global current_word, timer
    window.after_cancel(timer)
    current_word = rand.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_word["French"]}", fill="black")
    timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_word["English"]}")
    
# Is known

def is_known():
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_card()
    
window = Tk()
window.title("Namida")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263, image = card_front)
# Note: the fill black must be here or text won't show
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Right BTN
known_img = PhotoImage(file="images/right.png")
known_btn = Button(image=known_img, command=is_known, highlightthickness=0)
known_btn.grid(column=0, row=1)
# Wrong BTN
unknown_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=unknown_img, command=change_card, highlightthickness=0)
unknown_btn.grid(column=1, row=1)

change_card()

window.mainloop()