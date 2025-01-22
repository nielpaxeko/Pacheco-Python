from tkinter import *
from turtle import bgcolor
import requests
import pygame

pygame.mixer.init()
pygame.mixer.music.load("musashi_quotes/musashi-song.mp3")
pygame.mixer.music.play(loops=0)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")   
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    quote_text_content = f'{quote} - {author}'
    canvas.itemconfig(quote_text, text=quote_text_content)
    return quote_text_content



window = Tk()
window.title("Musashi Says...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", borderwidth=0, highlightthickness=0)
background_img = PhotoImage(file="musashi_quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click the button to get a quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="musashi_quotes/musashi.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, width=300)
kanye_button.grid(row=1, column=0)



window.mainloop()