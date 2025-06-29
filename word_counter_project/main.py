userText = input("Enter a text: ")


# ? get text words count
def get_text_words_count(text):
    words = text.split()
    return len(words)


# ? get text length
def get_text_length(text):
    return len(text)


print(
    f"Your text words: {get_text_words_count(userText)}\ntext lenght: {get_text_length(userText)}"
)
