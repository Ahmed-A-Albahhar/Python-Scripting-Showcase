BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random


try:
    data = pandas.read_csv('words_to_learn')

except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')

to_learn = data.to_dict(orient="records")
french_words = data.to_csv("data/french_words.csv", index=False)
french_words = pandas.read_csv("data/french_words.csv")
french_words = french_words["French"]
french_words = french_words.to_list()
word = random.choice(to_learn)
fr_word = word["French"]
en_word = word["English"]
def french_card():
    global en_word, update_card, fr_word, word
    window.after_cancel(id=update_card)
    canvas.itemconfig(card_image, image=card_front)
    word = random.choice(to_learn)
    fr_word = word["French"]
    en_word = word["English"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text= fr_word, fill="black")
    # print(word)
    # print(fr_word)
    # print(en_word)
    update_card = window.after(3000, english_card)


def english_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=en_word, fill="white")


def correct_answer():
    if fr_word in french_words:
        # print(f"This is the word to delete {fr_word}")
        french_words.remove(fr_word)
        to_learn.remove(word)
        words_to_learn = pandas.DataFrame(to_learn)
        words_to_learn.to_csv("data/word_to_learn.csv", index=False)


    french_card()


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background= BACKGROUND_COLOR)
card_back = PhotoImage(file="images\card_back.png")
card_front = PhotoImage(file="images\card_front.png")
canvas = Canvas(width=800, height=526, background= BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400,263, image= card_front)
card_title = canvas.create_text(400,150, text="Title", font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263, text= "Word", font=("Arial",60, "bold"))
correct = PhotoImage(file="images\correct.png")
wrong = PhotoImage(file="images\wrong.png")
correct_button = Button(image=correct, background= BACKGROUND_COLOR, highlightthickness=0, command=correct_answer)
wrong_button = Button(image= wrong, background= BACKGROUND_COLOR, highlightthickness=0, command=french_card)

canvas.grid(row=0,column=0, columnspan=2)
correct_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

update_card = window.after(3000, english_card)
french_card()


window.mainloop()
