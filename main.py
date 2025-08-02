from stats import num_words
from stats import char_counts
from stats import sorted_char_counts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words(text)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_counts(text):
        if char.isalpha():
            print(f"{char}: {count}")

main()