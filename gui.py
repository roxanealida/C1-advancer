''' A GUI for a vocabulary trainer'''
import random
import tkinter
import customtkinter


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


root = customtkinter.CTk()
root.title("Koalengua")
root.geometry("640x390")
root.minsize(640, 390)


root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((2, 3, 4, 5, 6, 7, 8), weight=0)


# global variables
LANGUAGE_TODAY = "some language"
MODE = 0
positions = []
WORD_LINE = "some word"
COUNTER = 0
counter_correct_words = 0

def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

# Create functions for each state of the buttons (normal/disabled) depending on whether
# the state is before the training, during the training, or after:

def beginning_state():
    '''this function gets called by the set_language function'''
    start_button.configure(text="START", state="normal")
    logo_label_trainer.configure(
        text="", font=customtkinter.CTkFont(size=15, weight="bold")
    )
    check_button.configure(state="disabled", text=" Check Word")
    set_state("disabled", exit_button)
    set_state("disabled", entry)


def training_state():
    ''' this function sets the state of check_button, entry, and exit_button to normal'''
    # this function gets called by the initialize function
    set_state("normal", check_button)
    set_state("normal", entry)
    set_state("normal", exit_button)


def exit_state():
    ''''this function is called with the exit button'''
    # this function gets called by the exit_button
    global counter_correct_words
    start_button.configure(text="START", state="disabled")
    logo_label_trainer.configure(
        text="", font=customtkinter.CTkFont(size=15, weight="bold")
    )
    check_button.configure(state="disabled", text="Check Word")
    set_state("normal", button_German, button_French, button_Spanish, button_Portuguese)
    logo_label_trainer.configure(
        text=(f"Great effort. Your score is {counter_correct_words}/{COUNTER}.")
    )
    entry.delete(0, tkinter.END)
    entry.configure(state="disabled")
    set_state("disabled", exit_button)
    counter_correct_words = 0



def radiobutton_event():
    '''function for radiobutton commands. repetition = 0, new words = 1'''
    global MODE
    MODE = radio_var.get()


def get_entry_value():
    '''function to return the string that is written in the entry:'''
    return entry.get()


class Language:
    '''class for Language attributes (their string representation and the list
    of their positions in either the dataframe or the files for the wrong words'''
    def _init_(self, language, positionlist):
        self.language = language
        self.positionlist = positionlist

    def set_language(self):
        '''this function sets the global variable LANGUAGE_TODAY to the language
    that is chosen with its button. It also disables all other language buttons.'''
        beginning_state()
        global LANGUAGE_TODAY
        global positions
        global COUNTER
        COUNTER = 0
        LANGUAGE_TODAY = self.language
        positions = self.positionlist
        set_state("normal", exit_button)
        if self.language == "German":
            set_state("disabled", button_French, button_Spanish, button_Portuguese)
        elif self.language == "French":
            set_state("disabled", button_German, button_Spanish, button_Portuguese)
        elif self.language == "Spanish":
            set_state("disabled", button_French, button_German, button_Portuguese)
        elif self.language == "Portuguese":
            set_state("disabled", button_French, button_Spanish, button_German)


# all language options initialized as objects:
German_object = Language("German", [1, 1])
French_object = Language("French", [2, 1])
Spanish_object = Language("Spanish", [3, 1])
Portuguese_object = Language("Portuguese", [4, 1])


def set_state(state_var, *args):
    '''helper function to set the state of various buttons at the same time'''
    for i in args:
        if state_var == "normal":
            i.configure(state="normal")
        elif state_var == "disabled":
            i.configure(state="disabled")


def initialize():
    '''function that gets called when the start_button is pressed.
    it opens the file (for new words the Df_translations.csv, repetition: 
    Wrong_words_{LANGUAGE_TODAY}) creates a random integer within the length
    of the files in order to find a random word to test logo_label_trainer 
    is updated to ask the user the word'''
    training_state()
    global COUNTER
    COUNTER += 1

    if MODE == 1:
        with open("Df_translations.csv", "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            position_of_language = positions[0]
    elif MODE == 0:
        with open(f"Wrong_words_{LANGUAGE_TODAY}.txt", "r", encoding="utf-8") as file2:
            lines = file2.read().splitlines()
            position_of_language = positions[1]

    rando = random.randint(
        0, (len(lines) - 1)
    )  # dynamic: length of lines of the text file/csv file
    global WORD_LINE

    WORD_LINE = lines[rando].split(",")
    global word
    word = WORD_LINE[position_of_language]
    if word[-1:] == "\n":
        word = word[:-1]
    logo_label_trainer.configure(
        trainerframe,
        text=f"What is the {LANGUAGE_TODAY} word for {WORD_LINE[0]}?",
        font=customtkinter.CTkFont(size=15, weight="bold"),
    )
    logo_label_trainer.grid(row=1, column=1, columnspan=2, padx=20, pady=(10, 10))
    start_button.configure(state="disabled")




def check_word_button():
    '''function that gets called by the check_button'''
    global COUNTER
    global counter_correct_words
    input1 = get_entry_value()

    if input1 == word:
        if logo_label_trainer.cget("text")[0:3] == "Wha":
            counter_correct_words += 1
            logo_label_trainer.configure(
                trainerframe,
                text="Good job! +1 point",
                font=customtkinter.CTkFont(size=15, weight="bold"),
            )
            logo_label_trainer.grid(row=1, column=1, columnspan=2, padx=20, pady=(10, 10))
            start_button.configure(
                text="New Word", font=customtkinter.CTkFont(size=13, weight="bold")
            )
            start_button.configure(state="normal")
            set_state("disabled", check_button)
            entry.delete(0, tkinter.END)
        else:
            logo_label_trainer.configure(
                trainerframe,
                text="Correct!",
                font=customtkinter.CTkFont(size=15, weight="bold"),
            )
            entry.delete(0, tkinter.END)
            set_state("disabled", check_button)

            start_button.configure(
                text="New Word", font=customtkinter.CTkFont(size=13, weight="bold")
            )
            start_button.configure(state="normal")

    elif input1 != word:
        with open(f"Wrong_words_{LANGUAGE_TODAY}.txt", "r+", encoding=":utf-8") as file:
            if f"{WORD_LINE[0]},{word}" not in file.read().splitlines():
                file.read()
                file.write(f"{WORD_LINE[0]},{word}\n")
        start_button.configure(
            text=f"{WORD_LINE[0]}", font=customtkinter.CTkFont(size=13, weight="bold")
        )
        if logo_label_trainer.cget("text")[0:3] == "Wha":
            entry.delete(0, tkinter.END)
            logo_label_trainer.configure(
                text=(f"Not correct. The word starts with {word[:2]}")
            )
        elif logo_label_trainer.cget("text")[0:3] == "Not":
            logo_label_trainer.configure(text=f"Type the word {word}.")
            entry.delete(0, tkinter.END)
        elif logo_label_trainer.cget("text")[0:3] in ["The", "Typ"]:
            logo_label_trainer.configure(
                text=(f"Still not correct. Type the word {word}.")
            )
            entry.delete(0, tkinter.END)
        elif logo_label_trainer.cget("text")[0:3] == "Sti":
            logo_label_trainer.configure(text=f"The word was {word}.")
            initialize()
            start_button.configure(
                text=f"{WORD_LINE[0]}",
                font=customtkinter.CTkFont(size=13, weight="bold"),
            )
            entry.delete(0, tkinter.END)

def check_word_enter(event):
    global counter_correct_words
    '''function that gets called by pressing enter'''
    input1 = get_entry_value()
    if logo_label_trainer.cget("text")[0:3] == "Goo":
        initialize()
    elif logo_label_trainer.cget("text")[0:3] == "Cor":
        initialize()
    elif input1 == word:
        if logo_label_trainer.cget("text")[0:3] == "Wha":
            counter_correct_words += 1
            logo_label_trainer.configure(
                trainerframe,
                text="Good job! +1 point",
                font=customtkinter.CTkFont(size=15, weight="bold"),
            )
            logo_label_trainer.grid(row=1, column=1, columnspan=2, padx=20, pady=(10, 10))
            entry.delete(0,tkinter.END)
            set_state("disabled", check_button)
            start_button.configure(
                text="New Word", font=customtkinter.CTkFont(size=13, weight="bold")
            )
            start_button.configure(state="normal")
        else:
            logo_label_trainer.configure(
                trainerframe,
                text="Correct!",
                font=customtkinter.CTkFont(size=15, weight="bold"),
            )
            entry.delete(0, tkinter.END)
            set_state("disabled", check_button)
            start_button.configure(
                text="New Word", font=customtkinter.CTkFont(size=13, weight="bold")
            )
            start_button.configure(state="normal")
    elif input1 != word:
        with open(f"Wrong_words_{LANGUAGE_TODAY}.txt", "r+", encoding=":utf-8") as file:
            if f"{WORD_LINE[0]},{word}" not in file.read().splitlines():
                file.read()
                file.write(f"{WORD_LINE[0]},{word}\n")
        start_button.configure(
            text=f"{WORD_LINE[0]}", font=customtkinter.CTkFont(size=13, weight="bold")
        )
        if logo_label_trainer.cget("text")[0:3] == "Wha":
            entry.delete(0, tkinter.END)
            logo_label_trainer.configure(
                text=(f"Not correct. The word starts with {word[:2]}")
            )
        elif logo_label_trainer.cget("text")[0:3] == "Not":
            logo_label_trainer.configure(text=f"Type the word {word}.")
            entry.delete(0, tkinter.END)
        elif logo_label_trainer.cget("text")[0:3] in ["The", "Typ"]:
            logo_label_trainer.configure(
                text=(f"Still incorrect. The word was {word}.")
            )
            entry.delete(0, tkinter.END)
        elif logo_label_trainer.cget("text")[0:3] == "Sti":
            initialize()
            start_button.configure(
                text=f"{WORD_LINE[0]}",
                font=customtkinter.CTkFont(size=13, weight="bold"),
            )
            entry.delete(0, tkinter.END)
# make the selection for the languages as well as the selection of MODE
# 1. frame

sidebar_frame = customtkinter.CTkFrame(root, corner_radius=30)
sidebar_frame.grid(row=0, column=0, rowspan=5, pady=20, padx=20)
sidebar_frame.grid_rowconfigure(5, weight=1)
logo_label = customtkinter.CTkLabel(
    sidebar_frame,
    text="Choose Language",
    font=customtkinter.CTkFont(size=15, weight="bold"),
)
logo_label.grid(row=0, column=0, padx=20, pady=(20, 0))


# 2. language buttons

button_German = customtkinter.CTkButton(
    sidebar_frame,
    text="German",
    command=German_object.set_language,
    state="normal",
    text_color_disabled="black",
)
button_German.grid(row=1, column=0, padx=10, pady=10)
button_French = customtkinter.CTkButton(
    sidebar_frame,
    text="French",
    command=French_object.set_language,
    state="normal",
    text_color_disabled="black",
)
button_French.grid(row=2, column=0, padx=10, pady=10)
button_Spanish = customtkinter.CTkButton(
    sidebar_frame,
    text="Spanish",
    command=Spanish_object.set_language,
    state="normal",
    text_color_disabled="black",
)
button_Spanish.grid(row=3, column=0, padx=10, pady=10)
button_Portuguese = customtkinter.CTkButton(
    sidebar_frame,
    text="Portuguese",
    command=Portuguese_object.set_language,
    state="normal",
    text_color_disabled="black",
)
button_Portuguese.grid(row=4, column=0, padx=10, pady=(10, 20))


# 3. radio buttons for the MODE

radio_var = tkinter.IntVar(value=0)
label_radio_group = customtkinter.CTkLabel(
    master=sidebar_frame,
    text="Learning mode",
    font=customtkinter.CTkFont(size=14, weight="bold"),
)
label_radio_group.grid(row=5, column=0, columnspan=1, padx=10, pady=0, sticky="")

radio_button_1 = customtkinter.CTkRadioButton(
    master=sidebar_frame,
    variable=radio_var,
    value=0,
    radiobutton_width=15,
    radiobutton_height=15,
    text="repetition",
    command=radiobutton_event,
)
radio_button_1.grid(row=6, column=0, pady=5, padx=20, sticky="n")

radio_button_2 = customtkinter.CTkRadioButton(
    master=sidebar_frame,
    variable=radio_var,
    value=1,
    radiobutton_width=15,
    radiobutton_height=15,
    text="new words",
    command=radiobutton_event,
)
radio_button_2.grid(row=7, column=0, pady=(0, 20), padx=20, sticky="n")

# TRAINERFRAME

trainerframe = customtkinter.CTkFrame(root, corner_radius=30)
trainerframe.grid(row=2, column=1, padx=(15, 40), pady=(20, 20))
logo_label_trainer = customtkinter.CTkLabel(
    trainerframe, text=" ", font=customtkinter.CTkFont(size=15, weight="bold")
)
logo_label_trainer.grid(row=3, column=1, columnspan=2, padx=20, pady=(10, 10))
trainerframe.grid_rowconfigure(1, weight=1)
trainerframe.grid_rowconfigure((2, 3), weight=0)
trainerframe.grid_rowconfigure((3, 4, 5, 6, 7, 8), weight=1)


# Elements in Trainerframe:
# 1. Start button
start_button = customtkinter.CTkButton(
    trainerframe,
    text="START",
    command=initialize,
    fg_color="green",
    state="disabled",
    text_color_disabled="grey",
    font=customtkinter.CTkFont(size=13, weight="bold"),
)
start_button.grid(row=0, column=1, padx=(20, 20), pady=20, columnspan=2)

# 2. Entry field
entry = customtkinter.CTkEntry(
    trainerframe,
    width=150,
    height=35,
    placeholder_text="Enter A Word",
    state="disabled",
    border_width=1,
)
entry.grid(row=4, column=1, pady=10, padx=20)
entry.bind('<Return>', check_word_enter)

# 3. Check word button
check_button = customtkinter.CTkButton(
    trainerframe,
    width=120,
    height=30,
    text="Check Word",
    command=check_word_button,
    state="disabled",
    text_color_disabled="grey",
    font=customtkinter.CTkFont(size=13, weight="bold"),
)
check_button.grid(row=4, column=2, padx=(0, 30))

# 4 Exit_button
exit_button = customtkinter.CTkButton(
    trainerframe,
    text="EXIT",
    state="disabled",
    command=exit_state,
    font=customtkinter.CTkFont(size=14, weight="bold"),
)
exit_button.grid(row=6, column=1, columnspan=2, pady=30)

root.mainloop()