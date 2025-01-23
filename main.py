#functions----------------------------------------------------
def main():#Returns the full book as a string
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def wordcount(whole_book):#Splits the string into words and counts the length
    words = whole_book.split()
    number = len(words)
    print(f"{number} words found in the document")

def character_count(whole_book):#Converts string into lower case and creates a dictionary of characters with an end total
    lower_words = whole_book.lower()
    characters = {}
    for char in lower_words:
        characters[char] = characters.get(char, 0) +1
    return characters

def convert_dict_to_list(char_dict):#turns dictionary into a list of dicts to be sorted
    char_list = []
    for char, num in char_dict.items():#loops through dictionary for characters and counts
        if char.isalpha():  # only include letters
            char_list.append({"char": char, "num": num})
    return char_list

def sort_on(dict):#working on
    return dict['num']

#Main code---------------------------------------------------
book = main()#stores main() in a variable to be used
print("--- Begin report of books/frankenstein.txt ---")
wordcount(book)
counts = character_count(book)#stores c_c() in a variable
chars_list = convert_dict_to_list(counts)
chars_list.sort(reverse=True, key=sort_on)#uses the sort on function to order our list
for char_dict in chars_list:
    print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
print("--- End report ---")#end report