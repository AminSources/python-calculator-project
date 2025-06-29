ones = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
teens = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
tens_digit = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def number_to_text(number):

    tens_digit_index = number // 10
    ones_digit_index = number % 10

    if number == 0:
        return ones[0]
    elif 1 <= number < 10:
        return ones[number]
    elif 10 <= number < 20:
        return teens[ones_digit_index]
    elif 20 <= number < 100:
        if ones_digit_index == 0:
            return tens_digit[tens_digit_index]
        else:
            return f"{tens_digit[tens_digit_index]} {ones[ones_digit_index]}"
    elif number == 100:
        return "one hundred"
    else:
        return "number is out of range"


# Test the function
for i in range(101):
    print(f"{i}: {number_to_text(i)}")
