from tkinter import *
import random

my_window = Tk()
my_window.geometry("400x200")
my_window.title("Guess the number Game")

def name():
    player_name = get()

heading = Label(my_window, text="Welcome to our game!", font=('Arial', 15))
heading.pack()

ask_for_name = Label(my_window, text="What's your name?", font=('Arial', 12))
ask_for_name.place(x=30, y=50)

name_answer = Entry(my_window)
name_answer.place(x=30, y= 70)

ask_for_guess = Label(my_window, text="Take a guess:", font=('Arial', 12))
ask_for_guess.place(x=30, y=100)

guess_answer = Entry(my_window)
guess_answer.place(x=30, y=120)

submit_name = Button(my_window, text="Ok", font=('Arial', 12))
submit_name.place(x=250, y=68)

submit_guess = Button(my_window, text="Guess", font=('Arial', 12))
submit_guess.place(x=250, y=118)

my_window.mainloop()