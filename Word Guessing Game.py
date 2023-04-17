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
    text.delete(0, tk.END)

# Clears input (for hard mode)   
def clear_text2(text):
    text.delete(0, tk.END)

# Game window
game = tk.Tk()

GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
WHITE = "#FFFFFF"
LIGHTGREEN = "#b7e4c7"
LIGHTRED = "#ff758f"
LIGHTORANGE = "#fec89a"

game.title("Word Guessing Game")
game.geometry("800x600")


def gamegui():
    global word_input
    global tries 
    global selected_word
    
    frame4 = tk.Frame(game)
    frame4.place(x=0, y=0, width=800, height=600)

    title0 = tk.Label(frame4, text='Word Guessing Game', font=('Arial', 20))
    title0.place(x=270, y=20)

    title0 = tk.Label(frame4, text='Level: Default', font=('Arial', 10,'bold'))
    title0.place(x=360, y=70)

    description = ttk.Label( frame4, text = "Please input a 5 letter word:",font=("Arial",7))
    description.place(x=343,y=390)
    tries = 0
    selected_word = str(select_word())

    # Input for word guess
    word_input = tk.Entry(frame4)
    word_input.place(x=343, y=405)
    word_input.focus()
    word_input.bind('<Return>', lambda event:word_guess_button.invoke())

    
    # Button to submit guess
    word_guess_button = tk.Button(frame4, text="Submit",cursor='hand2', command=lambda:[get_guess(), clear_text(word_input)])
    word_guess_button.place(x=380, y=435)

    # button to return to difficulty screen
    button_logout = tk.Button(game, text = "<--", command=difficulty)
    button_logout.place(x=0, y=0)

    
def get_guess():
    global xp
    global new_xp 
    global existing_xp

    sum = 0

    with open("valid-wordle-words.txt", "r") as file:
        allText = file.read()
        allowed = list(map(str, allText.split()))

    guessed_word = word_input.get().lower()

    global tries
    if tries < 5:

        # create new frame for each guess
        guess_frame = tk.Frame(game)
        guess_frame.place(x=320, y=110+50*tries , width=800, height=50)

        # Checks if length of words are the same
        if len(guessed_word) != len(selected_word):
            messagebox.showerror("Error", f"Word length is too short or too long.\nPlease input a {len(selected_word)}-letter word.")

        # Checks if word is valid
        if guessed_word not in allowed:
            messagebox.showerror("Error", "Word not in word list.")

        # Checks if both words are the same
        elif guessed_word == selected_word:

            for i, letter in enumerate(guessed_word):

                win = tk.Label(guess_frame, text=letter.upper(),font=('Arial', 10))
                win.grid(row=tries, column=i, padx=10, pady=10)
                win.config(bg=GREEN, fg=BLACK)

            xp = sum + 50

            # create a variable to check if the username exists or not
            username_exists = False
            with open("lvl_database.txt", "r+") as lvldatafile:
                lines = lvldatafile.readlines()
                # Iterate over the lines 
                # i represent the index of the current element
                # line represent the username item that added to cart
                # enumerate the function return an iterator that generate pair containing i and line
                # lines is the data inside the cart file
                for i, line in enumerate(lines):
                    if line.startswith(username):
                        xpParts = line.split(":")
                        existing_xp = xpParts[1].strip()
                        new_xp = int(existing_xp) + xp
                        new_line = f"{username}:{new_xp}\n"
                        lines[i] = new_line
                        # Set the flag to True
                        username_exists = True

                if not username_exists:
                    lvldatafile.write(f"{username}: {xp}\n")
                else:
                    # Go to the beginning of the file
                    lvldatafile.seek(0)
                    # Write the lines back to the file
                    lvldatafile.writelines(lines)
                    lvldatafile.close()

            messagebox.showinfo("Congratulations!", "You guessed the word!")
            pro_bargui(existing_xp)

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

                    label = tk.Label(guess_frame, text=a.upper(),font=('Arial', 10))
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
    frame4.place(x=0, y=0, width=800, height=600)
        
    tries = 0
    selected_word = str(select_word())

    title0 = tk.Label(frame4, text='Word Guessing Game', font=('Arial', 20))
    title0.place(x=270, y=10)

    title0 = tk.Label(frame4, text='Level: Easy', font=('Arial', 10,'bold'))
    title0.place(x=365, y=60)
    
    description = ttk.Label( frame4, text = "Please input a 5 letter word:",font=("Arial",7))
    description.place(x=343,y=485)

    # Input for word guess
    word_input = tk.Entry(frame4)
    word_input.place(x=343, y=500)
    word_input.focus()
    word_input.bind('<Return>', lambda event:word_guess_button.invoke())
    
    # Button to submit guess
    word_guess_button = tk.Button(frame4, text="Submit",cursor='hand2', command=lambda:[get_guess_easy(), clear_text(word_input)])
    word_guess_button.place(x=380, y=535)

    # button to return to difficulty screen
    button_logout = tk.Button(game, text = "<--", command=difficulty)
    button_logout.place(x=0, y=0)

# Game logic
def get_guess_easy():
    global xp
    global new_xp 
    global existing_xp
    sum = 0

    with open("valid-wordle-words.txt", "r") as file:
        allText = file.read()
        allowed = list(map(str, allText.split()))

    guessed_word = word_input.get().lower()

    global tries
    if tries < 10:
        guess_frame1 = tk.Frame(game)
        guess_frame1.place(x=320, y=80+40*tries, width=800, height=30)


        # Checks if length of words are the same
        if len(guessed_word) != len(selected_word):
            messagebox.showerror("Error", f"Word length is too short or too long.\nPlease input a {len(selected_word)}-letter word.")

        # Checks if word is valid
        if guessed_word not in allowed:
            messagebox.showerror("Error", "Word not in word list.")

        # Checks if both words are the same
        elif guessed_word == selected_word:

            for i, letter in enumerate(guessed_word):

                win = tk.Label(guess_frame1, text=letter.upper(),font=('Arial', 10))
                win.grid(row=tries, column=i, padx=10, pady=10)
                win.config(bg=GREEN, fg=BLACK)

            xp = sum + 25

              # create a variable to check if the username exists or not
            username_exists = False
            with open("lvl_database.txt", "r+") as lvldatafile:
                lines = lvldatafile.readlines()
                # Iterate over the lines 
                # i represent the index of the current element
                # line represent the username item that added to cart
                # enumerate the function return an iterator that generate pair containing i and line
                # lines is the data inside the cart file
                for i, line in enumerate(lines):
                    if line.startswith(username):
                        xpParts = line.split(":")
                        existing_xp = xpParts[1].strip()
                        new_xp = int(existing_xp) + xp
                        new_line = f"{username}:{new_xp}\n"
                        lines[i] = new_line
                        # Set the flag to True
                        username_exists = True

                if not username_exists:
                    lvldatafile.write(f"{username}: {xp}\n")
                else:
                    # Go to the beginning of the file
                    lvldatafile.seek(0)
                    # Write the lines back to the file
                    lvldatafile.writelines(lines)
                    lvldatafile.close()

            messagebox.showinfo("Congratulations!", "You guessed the word!")
            pro_bargui(existing_xp)

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

                    label = tk.Label(guess_frame1, text=a.upper(),font=('Arial', 10))
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
    frame4.place(x=0, y=0, width=800, height=600)

    title0 = tk.Label(frame4, text='Word Guessing Game', font=('Arial', 20))
    title0.place(x=270, y=20)

    title0 = tk.Label(frame4, text='Level: Hard', font=('Arial', 10,'bold'))
    title0.place(x=365, y=70)
    
    description = ttk.Label( frame4, text = "Please input a 7 letter word:",font=("Arial",7))
    description.place(x=343,y=390)
        
    tries = 0
    selected_word = str(select_word2())

    # Input for word guess
    word_input = tk.Entry(frame4)
    word_input.place(x=343, y=405)
    word_input.focus()
    word_input.bind('<Return>', lambda event:word_guess_button.invoke())
    
    # Button to submit guess
    word_guess_button = tk.Button(frame4, text="Submit",cursor='hand2', command=lambda:[get_guess_hard(username), clear_text2(word_input)])
    word_guess_button.place(x=380, y=435)

    # button to return to difficulty screen
    button_logout = tk.Button(game, text = "<--", command=difficulty)
    button_logout.place(x=0, y=0)

# Game logic
def get_guess_hard(username):
    global xp
    global new_xp 
    global existing_xp
    sum = 0

    with open("difficult-wordle-words.txt", "r") as file:
        allText = file.read()
        allowed = list(map(str, allText.split()))

    guessed_word = word_input.get().lower()

    global tries
    if tries < 5:
        guess_frame2 = tk.Frame(game)
        guess_frame2.place(x=290, y=110+50*tries, width=800, height=50)


        # Checks if length of words are the same
        if len(guessed_word) != len(selected_word):
            messagebox.showerror("Error", f"Word length is too short or too long.\nPlease input a {len(selected_word)}-letter word.")

        # Checks if word is valid
        if guessed_word not in allowed:
            messagebox.showerror("Error", "Word not in word list.")

        # Checks if both words are the same
        elif guessed_word == selected_word:

            for i, letter in enumerate(guessed_word):

                win = tk.Label(guess_frame2, text=letter.upper(),font=('Arial', 10))
                win.grid(row=tries, column=i, padx=10, pady=10)
                win.config(bg=GREEN, fg=BLACK)

            xp = sum + 100
            username_exists = False
            with open("lvl_database.txt", "r+") as lvldatafile:
                lines = lvldatafile.readlines()

                # Iterate over the lines 
                # i represent the index of the current element
                # line represent the username item that added to cart
                # enumerate the function return an iterator that generate pair containing i and line
                # lines is the data inside the cart file
                for i, line in enumerate(lines):
                    if line.startswith(username):
                        xpParts = line.split(":")
                        existing_xp = xpParts[1].strip()
                        new_xp = int(existing_xp) + xp
                        new_line = f"{username}:{new_xp}\n"
                        lines[i] = new_line
                        # Set the flag to True
                        username_exists = True
            

                if not username_exists:
                    lvldatafile.write(f"{username}: {xp}\n")

                else:
                    # Go to the beginning of the file
                    lvldatafile.seek(0)
                    # Write the lines back to the file
                    lvldatafile.writelines(lines)
                    lvldatafile.close()


            messagebox.showinfo("Congratulations!", "You guessed the word!")
            pro_bargui(existing_xp)

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

                    label = tk.Label(guess_frame2, text=a.upper(),font=('Arial', 10))
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



def pro_bargui(existing_xp):

    xp1 = int(existing_xp)
    frame25 = tk.Frame(game)
    frame25.place(x=0, y=0, width=800, height=600)
    xp_to_level_up = 100
    # Create a progressbar widget
    progress = ttk.Progressbar(frame25, orient="horizontal", length=300, mode="determinate")

    # Set the initial value of the progress bar based on starting XP
    progress["value"] = xp1 % xp_to_level_up

    # Place the progress bar on the window
    progress.place(relx=0.5, rely=0.5, anchor="center")

    # Create a label to display current level
    level_label = tk.Label(frame25, text=f"Level: {xp1//xp_to_level_up}",font=('Arial', 30))
    level_label.place(relx=0.5, rely=0.3, anchor="center")

    button1 = tk.Button(frame25, text=f"Next", command=lambda: pro_bar(new_xp,xp))
    button1.place(relx=0.5, rely=0.7, anchor="center")

    # Create a function that adds XP and checks if level up
    def pro_bar(new_xp,xp):
        xp2 = 100 - (xp1 % xp_to_level_up) 
        xp3 = 100 - (new_xp % 100)
        if xp == 100 or xp >= xp2 :
            # If level up, reset start XP to remaining XP and increase level by 1
            level_label.config(text=f"Level: {new_xp //100}")
            progress["value"] = new_xp % 100
            tk.messagebox.showinfo("Level Up!", f"You have reached level {int(new_xp / 100)}!")

        else:
            level_label.config(text=f"Level: {new_xp //100}")
            progress["value"] = new_xp % 100
            tk.messagebox.showinfo("Level Up!", f"You need {xp3} xp to reach next level!")
            

        button = tk.Button(frame25, text="                Back to Menu                ", command=lambda: difficulty())
        button.place(relx=0.5, rely=0.7, anchor="center")


# Login page
def login():
    global e1
    global e2
    frame1 = tk.Frame(game)
    frame1.place(x=0, y=0, width=800, height=600)

    title0 = tk.Label(frame1, text='Login Page', font=('Arial', 30))
    title0.place(x=305, y=80)

    user0 = tk.Label(frame1, text='Enter Username', font=('Arial', 10))
    user0.place(x=268, y=185)
    e1 = tk.Entry(frame1)
    e1.place(x=400, y=190)
    e1.focus()
    e1.bind('<Return>', lambda event: e2.focus())

    password0 = tk.Label(frame1, text='Enter Password', font=('Arial', 10))
    password0.place(x=270, y=250)
    e2 = tk.Entry(frame1)
    e2.place(x=400, y=255)
    e2.bind('<Return>', lambda event: b1.invoke())

    b0 = tk.Button(frame1, text='<--', cursor='hand2', command=sign_out)
    b0.place(x=0, y=0, width=35, height=35)
    b1 = tk.Button(frame1, text='Login', cursor='hand2', font=('Arial', 16), command=authentication)
    b1.place(x=360, y=320)
    
    ask0 = tk.Label(frame1, text="Don't have an account?", font=('Arial', 11))
    ask0.place(x=270, y=400)
    no_account = tk.Button(frame1, text="Sign up", cursor='hand2', border=0, font=('Arial', 11), fg='#57a1f8', command=signup)
    no_account.place(x=430, y=399)

# Login authentication function
# Login authentication function
def authentication():   
    db = open("database.txt","r")
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
    frame2.place(x=0, y=0, width=800, height=600)

    title1 = tk.Label(frame2, text='Signup Page', font=('Arial', 30))
    title1.place(x=285, y=80)

    user1 = tk.Label(frame2, text='Username', font=('Arial', 10))
    user1.place(x=270, y=185)
    e3 = tk.Entry(frame2)
    e3.place(x=400, y=190)
    e3.focus()
    e3.bind('<Return>', lambda event: e4.focus())
    
    password1 = tk.Label(frame2, text='Password', font=('Arial', 10))
    password1.place(x=272, y=250)
    e4 = tk.Entry(frame2)
    e4.place(x=400, y=255)
    e4.bind('<Return>', lambda event: e5.focus())

    conf_password = tk.Label(frame2, text='Confirm Password', font=('Arial', 10))
    conf_password.place(x=225, y=315)
    e5 = tk.Entry(frame2)
    e5.place(x=400, y=320)
    e5.bind('<Return>', lambda event: b3.invoke())

    b2 = tk.Button(frame2, text='<--', cursor='hand2', command=sign_out)
    b2.place(x=0, y=0, width=35, height=35)

    b3 = tk.Button(frame2, text='Signup', cursor='hand2', font=('Arial', 16), command=newaccount)
    b3.place(x=360, y=400)

# Signup new account function
def newaccount():
    db = open("database.txt", "r") #read the database textfile
    lvl_db = open("lvl_database.txt", "r")
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
            db = open("database.txt", "a+") 
            db.write(new_username+", "+new_password+"\n") #\n a type of escape character that will create a new line when used. 
            db.close()
            user_xp = "0"
            lvl_db = open ("lvl_database.txt","a+")
            lvl_db.write(new_username+":"+user_xp+"\n")
            lvl_db.close()
            if messagebox.askyesno("Access Permitted!", "Account created successfully! Do you wish to login?", icon='info') == True:
                login()
            else:
                home()   
            print("Success!")

def difficulty():
    frame10 = tk.Frame(game)
    frame10.place(x=0, y=0, width=800, height=600)

    # title
    title_label = ttk.Label(frame10, text = "Choose your Difficulty level", font = "Calibri 24 bold") # font = "font fontsize"
    title_label.pack(pady = 30)

    # difficulty descriptions
    # easy
    level_frame = ttk.Frame(frame10)
    button1 = tk.Button(
        level_frame,
        text = "EASY",
        height = 3,
        width = 8,
        background= LIGHTGREEN,
        font=('Calibri', 15, 'bold'), 
        cursor='hand2',
        command=gamegui_easy) # add command to go to hard lvl

    description = ttk.Label(
        level_frame, 
        text = "- Guess a 5 letter word\n- Complete within 10 tries")


    button1.pack(side = "left", padx = 20)
    description.pack(side = "right")
    level_frame.pack(pady = 20)

    #default
    level_frame = ttk.Frame(frame10)
    button = tk.Button(
        level_frame,
        text = "DEFAULT",
        height = 3,
        width = 8,
        background= LIGHTORANGE,
        font=('Calibri', 15, 'bold'), 
        cursor='hand2',
        command=gamegui) # add command to go to hard lvl

    description = ttk.Label(
        level_frame, 
        text = "- Guess a 5 letter word\n- Complete within 5 tries")

    button.pack(side = "left", padx = 15)
    description.pack(side = "left", padx = 5)
    level_frame.pack(pady = 20)

    # hard
    level_frame = ttk.Frame(frame10)
    button = tk.Button(
        level_frame,
        text = "HARD",
        height = 3,
        width = 8,
        background= LIGHTRED,
        font=('Calibri', 15, 'bold'),
        cursor='hand2',
        command=gamegui_hard) # add command to go to hard lvl

    description = ttk.Label(
        level_frame, 
        text = "- Guess a 7+ letter word\n- Complete within 5 tries")


    button.pack(side = "left", padx = 15)
    description.pack(side = "left", padx = 5)
    level_frame.pack(pady = 20)

    button_logout = tk.Button(frame10, text = "Log Out", command=sign_out)
    button_logout.place(x=0, y=0)

# Game rules
def rules():
    frame3 = tk.Frame(game)
    frame3.place(x=0, y=0, width=800, height=600)

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

    b5 = tk.Button(frame3, text='<--', cursor='hand2', command=sign_out)
    b5.place(x=0, y=0, width=35, height=35)
    b4 = tk.Button(frame3, text="I understand", cursor='hand2', font=('Arial', 15), command=difficulty)
    b4.place(x=330, y=380)

def leaderboard():
    frame35 = tk.Frame(game)
    frame35.place(x=0, y=0, width=800, height=600)
    line0 = tk.Label(frame35, text="Leaderboard", font=('Arial', 40))
    line0.place(x=255, y=30)

    b5 = tk.Button(frame35, text='<--', cursor='hand2', command=sign_out)
    b5.place(x=0, y=0, width=35, height=35)

    # create a custom style
    style = ttk.Style()
    # configure the Treeview background color in the style
    style.configure('Treeview', background='light blue',font=('Arial', 10,'bold'))
    style.configure('Treeview.Heading', font=('Arial', 16,'bold'))
    
    columns = ('Name', 'Score')
    leaderboard_tree = ttk.Treeview(frame35, columns=columns, show='headings')
    leaderboard_tree.pack()
    leaderboard_tree.place(x=300, y=150)
    
    # Define the column headings and their properties
    leaderboard_tree.heading('Name', text='Name',anchor='center' )
    leaderboard_tree.column('Name', width=100,anchor='center' )
    leaderboard_tree.heading('Score', text='Score',anchor='center')
    leaderboard_tree.column('Score', width=100,anchor='center')

    # Read the leaderboard data from the text file
    with open('lvl_database.txt', 'r') as f:
        leaderboard_data = [line.strip().split(':') for line in f]

    # Sort the leaderboard data based on the scores
    sorted_leaderboard_data = sorted(leaderboard_data, key=lambda x: int(x[1]), reverse=True)

    # Insert the sorted leaderboard data into the Treeview widget
    for i, (name, score) in enumerate(sorted_leaderboard_data):
        leaderboard_tree.insert('', tk.END, values=(name.upper(), score))
    


            
def sign_out():
    # clear the user's authentication status
    # for example, by setting a global variable to None
    global username
    username = None
    home()

# Quit function 
def quit():
    global game
    game.quit()

# GUI home page 
def home():
    label = tk.Label(game, text="Word Guessing Game", font=('Arial', 35))
    label.place(x=0, y=0, width=800, height=130)

    buttonframe0 = tk.Frame(game)
    buttonframe0.place(x=0, y=120, width=800, height=500)

    btn0 = tk.Button(buttonframe0, text='Login', cursor='hand2', font=('Arial', 25), command=login)
    btn0.pack()
    btn1 = tk.Button(buttonframe0, text='Register', cursor='hand2', font=('Arial', 25), command=signup)
    btn1.pack()
    btn2 = tk.Button(buttonframe0, text='Leaderboard', cursor='hand2', font=('Arial', 25), command=leaderboard)
    btn2.pack()
    btn3 = tk.Button(buttonframe0, text='Quit', cursor='hand2', font=('Arial', 25), command=quit)
    btn3.pack()

home()

# Game loop
game.mainloop()
