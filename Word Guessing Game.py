import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Randomly selects word
def select_word():
    with open("answerlist.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        return random.choice(words)
    
# Randomly selects word (for the hard mode)
def select_word2():
    with open("difficultanswerlist.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        return random.choice(words)
    
# Clears input    
def clear_text(text):
    text.delete(0, 5)

# Clears input (for hard mode)   
def clear_text2(text):
    text.delete(0, 7)

# Game window
game = tk.Tk()

GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
WHITE = "#FFFFFF"
LIGHTGREEN = "#b7e4c7"
LIGHTRED = "#ff758f"
LIGHTORANGE = "#fec89a"

game.title("Wordle")
game.geometry("800x500")
game.config(bg=BLACK)

def gamegui():
    global word_input
    global tries 
    global selected_word
    
    frame4 = tk.Frame(game)
    frame4.place(x=0, y=0, width=800, height=500)
    
    gametitle = tk.Label(frame4, text='Word Guessing Game', font=('Arial', 30))
    gametitle.pack(pady=25)
        
    tries = 0
    selected_word = str(select_word())

    # Input for word guess
    word_input = tk.Entry(frame4)
    word_input.place(x=315, y=330)
    
    # Button to submit guess
    word_guess_button = tk.Button(frame4, text="Submit", command=lambda:[get_guess(), clear_text(word_input)])
    word_guess_button.place(x=365, y=360)

    # button to return to difficulty screen
    button_logout = tk.Button(game, text = "<--", command=difficulty)
    button_logout.place(x=0, y=0)

# Game logic
def get_guess():
    with open("valid-wordle-words.txt", "r") as file:
        allText = file.read()
        allowed = list(map(str, allText.split()))

    guessed_word = word_input.get().lower()

    global tries
    if tries < 5:

        # Checks if length of words are the same
        if len(guessed_word) != len(selected_word):
            messagebox.showerror("Error", f"Word length is too short or too long.\nPlease input a {len(selected_word)}-letter word.")

        # Checks if word is valid
        if guessed_word not in allowed:
            messagebox.showerror("Error", "Word not in word list.")

        # Checks if both words are the same
        elif guessed_word == selected_word:

            for i, letter in enumerate(guessed_word):

                win = tk.Label(game, text=letter.upper())
                win.grid(row=tries, column=i, padx=10, pady=10)
                win.config(bg=GREEN, fg=BLACK)

            messagebox.showinfo("Congratulations!", "You guessed the word!")
            difficulty()

        # Checks if letters match
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

                    label = tk.Label(game, text=a.upper())
                    label.grid(row=tries, column=i, padx=10, pady=10)

                    # Letters match, same position
                    if a == b:
                        label.config(bg=GREEN, fg=BLACK)

                    # Letters match, wrong position
                    elif b == "$":
                        label.config(bg=YELLOW, fg=BLACK)

                    # Letters don't match            
                    else:
                        label.config(bg=BLACK, fg=WHITE)

            tries += 1

    # Game over
    if tries == 5:
        messagebox.showerror("You failed!", f"The word is {selected_word.upper()}")
        difficulty()

    

def gamegui_easy():
    global word_input
    global tries 
    global selected_word
    
    frame4 = tk.Frame(game)
    frame4.place(x=0, y=0, width=800, height=500)
    
    gametitle = tk.Label(frame4, text='Word Guessing Game', font=('Arial', 30))
    gametitle.pack(pady=15)
        
    tries = 0
    selected_word = str(select_word())

    # Input for word guess
    word_input = tk.Entry(frame4)
    word_input.place(x=315, y=405)
    
    # Button to submit guess
    word_guess_button = tk.Button(frame4, text="Submit", command=lambda:[get_guess_easy(), clear_text(word_input)])
    word_guess_button.place(x=365, y=435)

    # button to return to difficulty screen
    button_logout = tk.Button(game, text = "<--", command=difficulty)
    button_logout.place(x=0, y=0)

# Game logic
def get_guess_easy():

    with open("valid-wordle-words.txt", "r") as file:
        allText = file.read()
        allowed = list(map(str, allText.split()))

    guessed_word = word_input.get().lower()

    global tries
    if tries < 10:

        # Checks if length of words are the same
        if len(guessed_word) != len(selected_word):
            messagebox.showerror("Error", f"Word length is too short or too long.\nPlease input a {len(selected_word)}-letter word.")

        # Checks if word is valid
        if guessed_word not in allowed:
            messagebox.showerror("Error", "Word not in word list.")

        # Checks if both words are the same
        elif guessed_word == selected_word:

            for i, letter in enumerate(guessed_word):

                win = tk.Label(game, text=letter.upper())
                win.grid(row=tries, column=i, padx=10, pady=10)
                win.config(bg=GREEN, fg=BLACK)

            messagebox.showinfo("Congratulations!", "You guessed the word!")
            difficulty()

        # Checks if letters match
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

                    label = tk.Label(game, text=a.upper())
                    label.grid(row=tries, column=i, padx=10, pady=10)

                    # Letters match, same position
                    if a == b:
                        label.config(bg=GREEN, fg=BLACK)

                    # Letters match, wrong position
                    elif b == "$":
                        label.config(bg=YELLOW, fg=BLACK)

                    # Letters don't match            
                    else:
                        label.config(bg=BLACK, fg=WHITE)

            tries += 1
    
    # Game over
    if tries == 10:
        messagebox.showerror("You failed!", f"The word is {selected_word.upper()}")
        difficulty()


def gamegui_hard():
    global word_input
    global tries 
    global selected_word
    
    frame4 = tk.Frame(game)
    frame4.place(x=0, y=0, width=800, height=500)
    
    gametitle = tk.Label(frame4, text='Word Guessing Game', font=('Arial', 30))
    gametitle.pack(pady=25)
        
    tries = 0
    selected_word = str(select_word2())

    # Input for word guess
    word_input = tk.Entry(frame4)
    word_input.place(x=315, y=330)
    
    # Button to submit guess
    word_guess_button = tk.Button(frame4, text="Submit", command=lambda:[get_guess_hard(), clear_text2(word_input)])
    word_guess_button.place(x=365, y=360)

    # button to return to difficulty screen
    button_logout = tk.Button(game, text = "<--", command=difficulty)
    button_logout.place(x=0, y=0)

# Game logic
def get_guess_hard():

    with open("difficult-wordle-words.txt", "r") as file:
        allText = file.read()
        allowed = list(map(str, allText.split()))

    guessed_word = word_input.get().lower()

    global tries
    if tries < 5:

        # Checks if length of words are the same
        if len(guessed_word) != len(selected_word):
            messagebox.showerror("Error", f"Word length is too short or too long.\nPlease input a {len(selected_word)}-letter word.")

        # Checks if word is valid
        if guessed_word not in allowed:
            messagebox.showerror("Error", "Word not in word list.")

        # Checks if both words are the same
        elif guessed_word == selected_word:

            for i, letter in enumerate(guessed_word):

                win = tk.Label(game, text=letter.upper())
                win.grid(row=tries, column=i, padx=10, pady=10, x=365, y=120)
                win.config(bg=GREEN, fg=BLACK)

            messagebox.showinfo("Congratulations!", "You guessed the word!")
            difficulty()

        # Checks if letters match
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

                    label = tk.Label(game, text=a.upper())
                    label.grid(row=tries, column=i, padx=10, pady=10)

                    # Letters match, same position
                    if a == b:
                        label.config(bg=GREEN, fg=BLACK)

                    # Letters match, wrong position
                    elif b == "$":
                        label.config(bg=YELLOW, fg=BLACK)

                    # Letters don't match            
                    else:
                        label.config(bg=BLACK, fg=WHITE)

            tries += 1

    # Game over
    if tries == 5:
        messagebox.showerror("You failed!", f"The word is {selected_word.upper()}")
        difficulty()

    

# Login page
def login():
    global e1
    global e2
    frame1 = tk.Frame(game)
    frame1.place(x=0, y=0, width=800, height=500)

    title0 = tk.Label(frame1, text='Login Page', font=('Arial', 30))
    title0.place(x=305, y=30)

    user0 = tk.Label(frame1, text='Enter Username', font=('Arial', 10))
    user0.place(x=268, y=135)
    e1 = tk.Entry(frame1)
    e1.place(x=400, y=140)

    password0 = tk.Label(frame1, text='Enter Password', font=('Arial', 10))
    password0.place(x=270, y=200)
    e2 = tk.Entry(frame1)
    e2.place(x=400, y=205)

    b0 = tk.Button(frame1, text='<--', cursor='hand2', command=home)
    b0.place(x=0, y=0, width=35, height=35)
    b1 = tk.Button(frame1, text='Login', cursor='hand2', font=('Arial', 16), command=authentication)
    b1.place(x=360, y=270)
    
    ask0 = tk.Label(frame1, text="Don't have an account?", font=('Arial', 11))
    ask0.place(x=270, y=350)
    no_account = tk.Button(frame1, text="Sign up", cursor='hand2', border=0, font=('Arial', 11), fg='#57a1f8', command=signup)
    no_account.place(x=430, y=349)

# Login authentication function
# Login authentication function
def authentication():   
    db = open("database.py","r")
    global username
    username = e1.get()
    password = e2.get()  
    
    d = [] #empty list to store Username
    p = [] #empty list to store password
    for i in db: #to split my text in database
        a,b = i.split(",")
        b = b.strip() #to remove the character infront the username so that username can stand alone
        #append the usename and password into the text file
        d.append(a)
        p.append(b)
    data = dict(zip(d, p))# make it to the pair and read the data

    try:
        if data[username]:
        #if data contain the username try following
                if password == data[username]:
                #check if password and username is it match
                    rules()

                else:
                    if messagebox.askyesno("Error", "Password or Username incorrect. Do you want to try again?", icon='error') == True:
                        login()
                    else:
                        home()
                    
        else:
            if messagebox.askyesno("Error", "Username or password doesn't exist. Do you want to try again?", icon='error') == True:
                login()
            else:
                home()
    except:
        if messagebox.askyesno("Error", "Username or password doesn't exist. Do you want to try again?", icon='error') == True:
            login()
        else:
            home()    

# Signup interface
def signup():
    global e3
    global e4
    global e5
    
    frame2 = tk.Frame(game)
    frame2.place(x=0, y=0, width=800, height=500)

    title1 = tk.Label(frame2, text='Signup Page', font=('Arial', 30))
    title1.place(x=285, y=30)

    user1 = tk.Label(frame2, text='Username', font=('Arial', 10))
    user1.place(x=270, y=135)
    e3 = tk.Entry(frame2)
    e3.place(x=400, y=140)

    password1 = tk.Label(frame2, text='Password', font=('Arial', 10))
    password1.place(x=272, y=200)
    e4 = tk.Entry(frame2)
    e4.place(x=400, y=205)

    conf_password = tk.Label(frame2, text='Confirm Password', font=('Arial', 10))
    conf_password.place(x=225, y=265)
    e5 = tk.Entry(frame2)
    e5.place(x=400, y=270)

    b2 = tk.Button(frame2, text='<--', cursor='hand2', command=home)
    b2.place(x=0, y=0, width=35, height=35)
    b3 = tk.Button(frame2, text='Signup', cursor='hand2', font=('Arial', 16), command=newaccount)
    b3.place(x=360, y=350)

# Signup new account function
def newaccount():
    db = open("database.py", "r") #read the database textfile
    lvl_db = open("lvl_database.py", "r")
    new_username = e3.get()
    new_password = e4.get()
    new_conf_password = e5.get()
        
    d = [] #empty list to store Username
    p = [] #empty list to store password
    for i in db: #to split my text in database
        a,b = i.split(",")
        b = b.strip() #to remove the character infront the username so that username can stand alone
        #append the usename and password into the text file
        d.append(a)
        p.append(b)
    data = dict(zip(d, p))# make it to the pair and read the data 

    if(new_password != new_conf_password): 
        if messagebox.askyesno("Access Denied", "Passswords must match. Do you wish to try again?", icon='error') == True:
            signup()
        else:
            home()

    else:
        #Deny user to proceed if the password doesn't match the requirement.
        if len(new_password) < 6:
            if messagebox.askyesno("Access Denied", "Password length should be between 6-8 characters. Do you wish to try again?", icon='error') == True:
                signup()
            else:
                home()
                
        elif len(new_password) > 8:
            if messagebox.askyesno("Access Denied", "Password length should be between 6-8 characters. Do you wish to try again?", icon='error') == True:
                signup()
            else:
                home()        
        
        #Deny user to proceed if the username already exists in the "d" text file
        elif new_username in d:
            if messagebox.askyesno("Access Denied", "Username already exists. Do you wish to try again?", icon='error') == True:
                signup()
            else:
                home()    

        # Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. 
        # If the file does not exist, it creates a new file for reading and writing.    
        else:
            db = open("database.py", "a+") 
            db.write(new_username+", "+new_password+"\n") #\n a type of escape character that will create a new line when used. 
            db.close()
            user_xp = "0"
            lvl_db = open("lvl_database.py", "a+")
            lvl_db.write(new_username+", "+user_xp+"\n")
            lvl_db.close()
            if messagebox.askyesno("Access Permitted!", "Account created successfully! Do you wish to login?", icon='info') == True:
                login()
            else:
                home()   
            print("Success!")

def difficulty():
    frame = tk.Frame(game)
    frame.place(x=0, y=0, width=800, height=500)

    # title
    title_label = ttk.Label(frame, text = "Choose your Difficulty level", font = "Calibri 24 bold") # font = "font fontsize"
    title_label.pack(pady = 30)

    # difficulty descriptions
    # easy
    level_frame = ttk.Frame(frame)
    button1 = tk.Button(
        level_frame,
        text = "EASY",
        height = 3,
        width = 8,
        background= LIGHTGREEN,
        font=('Calibri', 15, 'bold'), 
        command=gamegui_easy) # add command to go to hard lvl

    description = ttk.Label(
        level_frame, 
        text = "- Guess a 5 letter word\n- Complete within 10 tries")


    button1.pack(side = "left", padx = 20)
    description.pack(side = "right")
    level_frame.pack(pady = 20)

    #default
    level_frame = ttk.Frame(frame)
    button = tk.Button(
        level_frame,
        text = "DEFAULT",
        height = 3,
        width = 8,
        background= LIGHTORANGE,
        font=('Calibri', 15, 'bold'), command=gamegui) # add command to go to hard lvl

    description = ttk.Label(
        level_frame, 
        text = "- Guess a 5 letter word\n- Complete within 5 tries")

    button.pack(side = "left", padx = 15)
    description.pack(side = "left", padx = 5)
    level_frame.pack(pady = 20)

    # hard
    level_frame = ttk.Frame(frame)
    button = tk.Button(
        level_frame,
        text = "HARD",
        height = 3,
        width = 8,
        background= LIGHTRED,
        font=('Calibri', 15, 'bold'),
        command=gamegui_hard) # add command to go to hard lvl

    description = ttk.Label(
        level_frame, 
        text = "- Guess a 7+ letter word\n- Complete within 5 tries")


    button.pack(side = "left", padx = 15)
    description.pack(side = "left", padx = 5)
    level_frame.pack(pady = 20)

    button_logout = tk.Button(frame, text = "Log Out", command=home)
    button_logout.place(x=0, y=0)

# Game rules
def rules():
    frame3 = tk.Frame(game)
    frame3.place(x=0, y=0, width=800, height=500)

    line0 = tk.Label(frame3, text="Game Rules", font=('Arial', 30))
    line0.place(x=280, y=30)
    line1 = tk.Label(frame3, text='There are a few rules players should know of before playing the game:', font=('Arial', 14))
    line1.place(x=100, y=100)
    line2 = tk.Label(frame3, text='1. Players are not allowed to search for any type of clues online to win the game.', font=('Arial', 13))
    line2.place(x=100, y=150)
    line3 = tk.Label(frame3, text='2. A correct letter placed in the correct order will turn into GREEN', font=('Arial', 13))
    line3.place(x=100, y=190)
    line4 = tk.Label(frame3, text='3. A correct letter placed in the wrong order will turn into YELLOW', font=('Arial', 13))
    line4.place(x=100, y=230)
    line5 = tk.Label(frame3, text='4. An incorrect letter will turn into BLACK', font=('Arial', 13))
    line5.place(x=100, y=270)
    line6 = tk.Label(frame3, text='5. Answers are NEVER plurals', font=('Arial', 13))
    line6.place(x=100, y=310)

    b5 = tk.Button(frame3, text='<--', cursor='hand2', command=home)
    b5.place(x=0, y=0, width=35, height=35)
    b4 = tk.Button(frame3, text="I understand", cursor='hand2', font=('Arial', 15), command=difficulty)
    b4.place(x=330, y=380)

# Quit function 
def quit():
    global game
    game.quit()

# GUI home page 
def home():
    label = tk.Label(game, text="Word Guessing Game", font=('Arial', 25))
    label.place(x=0, y=0, width=800, height=130)

    buttonframe0 = tk.Frame(game)
    buttonframe0.place(x=0, y=120, width=800, height=500)

    btn0 = tk.Button(buttonframe0, text='Login', cursor='hand2', font=('Arial', 20), command=login)
    btn0.pack()
    btn1 = tk.Button(buttonframe0, text='Register', cursor='hand2', font=('Arial', 20), command=signup)
    btn1.pack()
    btn3 = tk.Button(buttonframe0, text='Quit', cursor='hand2', font=('Arial', 20), command=quit)
    btn3.pack()

home()

# Game loop
game.mainloop()
