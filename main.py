def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def wordcount(whole_book):
    words = whole_book.split()
    number = len(words)
    print(number)

def character_count(whole_book):
    lower_words = whole_book.lower()
    characters = {}
    for char in lower_words:
        characters[char] = characters.get(char, 0) +1
    return characters

book = main()
wordcount(book)
counts = character_count(book)
for char, count in counts.items():
    print(f"'{char}': {count}")