from tkinter import *
import requests


def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title('Kanye Says...')
window.config(padx=40, pady=40, bg='white')
photo_image = PhotoImage(file='background.png')
canvas = Canvas(width=300, height=414, bg='white', highlightthickness=0)
canvas.grid(row=0, column=0)
canvas.create_image(150, 207, image=photo_image)
quote_text = canvas.create_text(150, 190, text='', font=('Ariel', 16, 'bold'), width=280)

btn_img = PhotoImage(file='kanye.png')
kanye_button = Button(image=btn_img, bg='white', highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
