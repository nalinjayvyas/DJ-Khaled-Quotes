from tkinter import *
import pygame

BACK_GROUND = "#FFE3B3"
FORE_GROUND = "#53D2DC"

pygame.mixer.init()
window = Tk()
window.title("DJ Khaled Quotes")
window.config(bg=BACK_GROUND,padx=30,pady=30)

def next_quote():
    pygame.mixer.music.load("Dj-Khaled_audio.mp3")
    pygame.mixer.music.play()

canvas = Canvas(width=400, height=300, bg=FORE_GROUND, border=0,borderwidth=0,background=FORE_GROUND,
                highlightbackground=FORE_GROUND)
quote_text = canvas.create_text(200,150, text="placeholder ", font=("Arial",18,"bold"), fill=BACK_GROUND,
                                width=200)
quote_img = PhotoImage(file="./Quotes.png",width=360,height=360)
canvas.create_image(200,150, image=quote_img)
canvas.grid(row=0, column=0,pady=50)


khaled_img = PhotoImage(file="./DJ-Khaled.png",width=225, height=224)
button = Button(image=khaled_img, highlightthickness=0, borderwidth=0,border=0,bg=BACK_GROUND
                ,background=BACK_GROUND,activebackground=BACK_GROUND, command=next_quote)
button.grid(row=1, column=0)




window.mainloop()