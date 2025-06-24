from tkinter import *

# * app main window ==========================================================================
root = Tk()
root.title("Calculator App")
root.geometry("300x400")
root.resizable(False, False)

# * app variables ===========================================================================
result = 0
inputValue = IntVar()
calculatorSign = ["+", "-", "/", "*"]

# * app functions ============================================================================


def calculate():
    value = numberEntry.get()
    result = eval(value)

    resultLabel.config(text=result)


def addSign(sign):
    value = list(numberEntry.get())

    if value[-1] in calculatorSign:
        pass
    else:
        numberEntry.insert(END, sign)


# * app ui ===================================================================================
numberLabel = Label(
    root,
    text="Enter Number:",
)
numberLabel.pack(
    padx=20,
    pady=0,
    anchor="nw",
)

numberEntry = Entry(root, textvariable=inputValue)
numberEntry.pack(
    padx=20,
    pady=10,
    fill="x",
    anchor="nw",
)

resualtFrame = Frame(root, height=20)
resualtFrame.pack(
    padx=20,
    pady=10,
    fill="x",
    anchor="nw",
)

resultTextLabel = Label(
    resualtFrame,
    text="Result:",
).grid(row=0, column=0)

resultLabel = Label(
    resualtFrame,
    text=result,
)
resultLabel.grid(row=0, column=1)

actionsLabel = Label(root, text="Select Actions:").pack(
    padx=20,
    pady=0,
    anchor="nw",
)

actionsFrame = Frame(
    root,
)
actionsFrame.pack(
    padx=20,
    pady=20,
    expand=True,
    fill="both",
)

sumButton = Button(
    actionsFrame,
    text="+",
    command=lambda: addSign("+"),
)
sumButton.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

minusButton = Button(
    actionsFrame,
    text="-",
    command=lambda: addSign("-"),
)
minusButton.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

multiplyButton = Button(
    actionsFrame,
    text="*",
    command=lambda: addSign("*"),
)
multiplyButton.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

divideButton = Button(
    actionsFrame,
    text="/",
    command=lambda: addSign("/"),
)
divideButton.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

actionsFrame.columnconfigure(0, weight=1)
actionsFrame.columnconfigure(1, weight=1)
actionsFrame.rowconfigure(0, weight=1)
actionsFrame.rowconfigure(1, weight=1)

calculateButton = Button(root, text="Calculate", command=lambda: calculate()).pack(
    padx=20,
    pady=10,
    fill="x",
    anchor="nw",
)


if __name__ == "__main__":
    # ? run the app
    root.mainloop()
