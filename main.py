from tkinter import *
import random
import tkinter.messagebox
my_window = Tk()
my_window.geometry("400x200")
my_window.title("Guess the number Game")

def name():
    player_name = name_answer.get()
    tkinter.messagebox.showinfo("Hi " + player_name + "I'm guessing a number between 1 and 20" )

def check_num():
    guess = text_guess.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("high", "Your guess is too high!")
    if guess < number:
        tkinter.messagebox.showinfo("low", "Your guess is too low!")
    if guess == number:
        tkinter.messagebox.showinfo("good", "Good Job!")  

ask_for_name = Label(my_window, text="What's your name?", font=('Arial', 12))
ask_for_name.place(x=30, y=50)

name_answer = Entry(my_window)
name_answer.place(x=30, y= 70)

ask_for_guess = Label(my_window, text="Take a guess:", font=('Arial', 12))
ask_for_guess.place(x=30, y=100)

guess_answer = Entry(my_window)
guess_answer.place(x=30, y=120)

submit_name = Button(my_window, text="Ok", font=('Arial', 12), command = name)
submit_name.place(x=250, y=68)

submit_guess = Button(my_window, text="Guess", font=('Arial', 12), command = check_num)
submit_guess.place(x=250, y=118)

my_window.mainloop()