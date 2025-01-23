def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def wordcount(whole_book):
    words = whole_book.split()
    number = len(words)
    print(number)

book = main()
wordcount(book)