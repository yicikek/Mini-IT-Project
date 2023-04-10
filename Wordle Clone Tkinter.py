import random
import os
from tkinter import *
from tkinter import messagebox

# Clears screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Randomly selects word
def select_word():
    with open("answerlist.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        return random.choice(words)
    
def clear_text(text):
    text.delete(0, END)

# Start
clear()

game = Tk()

GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
WHITE = "#FFFFFF"

game.title("Wordle")
game.geometry("500x600")
game.config(bg=BLACK)

tries = 0
selected_word = str(select_word())

word_input = Entry(game)
word_input.grid(row=999, column=0, columnspan=3, padx=10, pady=10)

def get_guess():

    with open("valid-wordle-words.txt", "r") as file:
        allText = file.read()
        allowed = list(map(str, allText.split()))

    global selected_word
    guessed_word = word_input.get().lower()

    messagebox.showinfo(selected_word)

    global tries

    if tries < 5:

        if len(guessed_word) != len(selected_word):
            messagebox.showerror("Error", f"Word length is too short or too long.\nPlease input a {len(selected_word)}-letter word.")

        if guessed_word not in allowed:
            messagebox.showerror("Error", "Word not in word list.")

        elif guessed_word == selected_word:

            for i, letter in enumerate(guessed_word):

                win = Label(game, text=letter.upper())
                win.grid(row=tries, column=i, padx=10, pady=10)
                win.config(bg=GREEN, fg=BLACK)

            messagebox.showinfo("Congratulations!", "You guessed the word!")

        else:

            feedback = []
            guess_list = [*guessed_word]
            select_list = [*selected_word]

            for letter in range(len(guessed_word)):

                if guessed_word.lower()[letter] == selected_word[letter]:
                    feedback.append(guessed_word[letter])
                    guess_list[letter] = "placeholder1"
                    select_list[letter] = "placeholder2"

                else:
                    feedback.append("#")

            for index, letter in enumerate(guess_list):

                if letter in select_list:
                    feedback[index] = "$"
                    select_list.remove(letter)

            guess_list = [*guessed_word]

            for i, (a, b) in enumerate(zip(guess_list, feedback)):

                    label = Label(game, text=a.upper())
                    label.grid(row=tries, column=i, padx=10, pady=10)

                    if a == b:
                        label.config(bg=GREEN, fg=BLACK)

                    elif b == "$":
                        label.config(bg=YELLOW, fg=BLACK)
                                
                    else:
                        label.config(bg=BLACK, fg=WHITE)

            tries += 1

    if tries == 5:
        messagebox.showerror("You failed!", f"The word is {selected_word.upper()}")

word_guess_button = Button(game, text="Submit", command=lambda:[get_guess(), clear_text(word_input)])
word_guess_button.grid(row=999, column=3, columnspan=2)

game.mainloop()