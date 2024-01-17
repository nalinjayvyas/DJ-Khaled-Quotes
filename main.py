from tkinter import *
import pygame
import random

BACK_GROUND = "#FFE3B3"
FORE_GROUND = "#53D2DC"

# Initializing Pygame Mixer for audio
pygame.mixer.init()

# Creating a Tkinter Window
window = Tk()
window.title("DJ Khaled Quotes")
window.config(bg=BACK_GROUND, padx=30, pady=30)

# Reading quotes data and saving a list called data
with open("./quotes.txt", "r") as file:
    data = file.readlines()

# Command function to generate next quote
def next_quote():
    quote = random.choice(data)
    canvas.itemconfig(quote_text, text=quote, fill=BACK_GROUND, font=("Arial", 16, "bold"), width=400)
    pygame.mixer.music.load("Dj-Khaled_audio.mp3")
    pygame.mixer.music.play()


# Creating a canvas object
canvas = Canvas(width=500, height=400, bg=FORE_GROUND, border=0, borderwidth=0, background=FORE_GROUND,
                highlightbackground=FORE_GROUND)
quote_text = canvas.create_text(250, 200, text="🎵🎵We the Best Music🎵🎵",
                                font=("Arial", 16, "bold"), fill=BACK_GROUND, width=400)
quote_img = PhotoImage(file="./Quotes.png", width=500, height=500)
canvas.create_image(250, 200, image=quote_img)
canvas.grid(row=0, column=0, pady=50)

# Creating the DJ Khaled Button
khaled_img = PhotoImage(file="./DJ-Khaled.png", width=225, height=224)
button = Button(image=khaled_img, highlightthickness=0, borderwidth=0, border=0,bg=BACK_GROUND
                , background=BACK_GROUND,activebackground=BACK_GROUND, command=next_quote)
button.grid(row=1, column=0)

# Looping main window
window.mainloop()
