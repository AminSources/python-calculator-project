#
# ? python unit converter app project
# ? developed by Mohammad Amin Farshbaf. 2025-6-25 10:05 PM

from tkinter import *
from tkinter import ttk

# ? app main window
root = Tk()
root.title("Unit Converter App")
root.resizable(False, False)
root.geometry("325x200")

# * app variables
unitsListValue1 = StringVar()
unitsListValue2 = StringVar()
unitValue1 = DoubleVar()
unitValue2 = DoubleVar()
lenghtUnits = ["meters", "centimeters", "inches", "feet", "yards", "miles"]
weightUnits = ["kilograms", "pounds", "ounces", "grams"]


# * app functions
def convertUnits():
    unit1 = unitsList1.get()
    unit2 = unitsList2.get()

    if unit1 in lenghtUnits and unit2 in lenghtUnits:
        lengthConversion(unit1, unit2)
    elif unit1 in weightUnits and unit2 in weightUnits:
        weightConversion(unit1, unit2)
    else:
        raise ValueError("Invalid unit conversion")


def lengthConversion(unit1, unit2):
    value = unitValue1.get()

    # Conversion factors to meters
    to_m = {
        "meters": 1,
        "centimeters": 0.01,
        "inches": 0.0254,
        "feet": 0.0254 * 12,
        "yards": 0.0254 * 36,
        "miles": 0.000621371192,
    }
    # Conversion factors from meters to target unit
    from_m = {
        "meters": 1,
        "centimeters": 100,
        "inches": 39.37007874,
        "feet": 3.28084,
        "yards": 1.0936133,
        "miles": 0.621371192,
    }

    if unit1 in to_m and unit2 in from_m:
        value_in_m = value * to_m[unit1]
        converted_value = value_in_m * from_m[unit2]
        unitValue2.set(converted_value)
    elif unit1 == unit2:
        unitValue2.set(value)
    else:
        raise ValueError("Invalid unit conversion")


def weightConversion(unit1, unit2):
    unit1 = unitsList1.get()
    unit2 = unitsList2.get()
    value = unitValue1.get()

    # Conversion factors to kilograms
    to_kg = {
        "kilograms": 1,
        "grams": 0.001,
        "ounces": 0.028349523125,
        "pounds": 0.45359237,
    }
    # Conversion factors from kilograms to target unit
    from_kg = {
        "kilograms": 1,
        "grams": 1000,
        "ounces": 35.27396195,
        "pounds": 2.2046226218,
    }

    if unit1 in to_kg and unit2 in from_kg:
        value_in_kg = value * to_kg[unit1]
        converted_value = value_in_kg * from_kg[unit2]
        unitValue2.set(converted_value)
    elif unit1 == unit2:
        unitValue2.set(value)
    else:
        raise ValueError("Invalid unit conversion")


# * app ui
unitValueFrame1 = ttk.Frame(root)
unitValueFrame1.grid(row=0, column=0, padx=10, pady=10)

unitValueLabel1 = Label(unitValueFrame1, text="Enter Value")
unitValueLabel1.pack(
    anchor="nw",
)

unitValueEntry1 = Entry(unitValueFrame1, width=23, textvariable=unitValue1)
unitValueEntry1.pack(anchor="nw", pady=5)

unitValueFrame2 = ttk.Frame(root)
unitValueFrame2.grid(row=0, column=1, padx=10, pady=10)

unitValueLabel2 = Label(unitValueFrame2, text="Calculated value:")
unitValueLabel2.pack(anchor="nw")

unitValueEntry2 = Entry(
    unitValueFrame2, state="readonly", width=23, textvariable=unitValue2
)
unitValueEntry2.pack(anchor="nw", pady=5)

unitsFrame1 = ttk.Frame(root)
unitsFrame1.grid(row=1, column=0, padx=10, pady=10)

unitsTitle1 = Label(unitsFrame1, text="Convert From")
unitsTitle1.pack(anchor="nw")

unitsList1 = ttk.Combobox(
    unitsFrame1,
    textvariable=unitsListValue1,
    values=[
        "kilograms",
        "grams",
        "ounces",
        "pounds",
        "meters",
        "centimeters",
        "inches",
        "feet",
        "yards",
        "miles",
    ],
)
unitsList1.pack(anchor="nw", pady=5)

unitsFrame2 = ttk.Frame(root)
unitsFrame2.grid(row=1, column=1, padx=10, pady=10)

unitsTitle2 = Label(unitsFrame2, text="Convert To")
unitsTitle2.pack(anchor="nw")

unitsList2 = ttk.Combobox(
    unitsFrame2,
    textvariable=unitsListValue2,
    values=[
        "kilograms",
        "grams",
        "ounces",
        "pounds",
        "meters",
        "centimeters",
        "inches",
        "feet",
        "yards",
        "miles",
    ],
)
unitsList2.pack(anchor="nw", pady=5)

calculateButton = ttk.Button(root, text="Calculate", command=lambda: convertUnits())
calculateButton.grid(
    row=2,
    columnspan=2,
    padx=10,
    pady=10,
)


# ? main loop
if __name__ == "__main__":
    root.mainloop()
