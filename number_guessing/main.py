#
# ? python calculator app project
# ? developed by Mohammad Amin Farshbaf. 2025-6-25 11:07 PM

import random
from tkinter import *

# ? app main windows
root = Tk()
root.title("Number Guessing Game")
root.geometry("300x200")
root.resizable(False, False)

# * app variables
randomNumber = random.randint(1, 100)
guessEntryValue = IntVar()


# * app functions
def checkGuess():
    guessCount = int(guessEntry.get())

    if guessCount < 100 and guessCount >= 1:
        if guessCount == randomNumber:
            guessResultLabel.config(
                text="Congratulations!\nYou guessed the correct number.",
                foreground="green",
            )
        elif guessCount > randomNumber:
            guessResultLabel.config(text="Too high! Try again.", foreground="black")
        elif guessCount < randomNumber:
            guessResultLabel.config(text="Too low! Try again.", foreground="black")
    else:
        guessResultLabel.config(
            text="Invalid input!\nPlease enter a number between 1 and 100.",
            foreground="red",
        )


# * app ui
numberLabel = Label(root, text="Guess a number between 1 and 100!")
numberLabel.pack(padx=10, pady=10, anchor="nw")

guessEntry = Entry(root, textvariable=guessEntryValue)
guessEntry.pack(padx=10, pady=10, fill="x")

guessResultLabel = Label(root, text="")
guessResultLabel.pack(padx=10, pady=10)

guessButton = Button(root, text="Guess", width=15, command=lambda: checkGuess())

guessButton.pack(padx=10, pady=10)

# ? main loop
if __name__ == "__main__":
    root.mainloop()
