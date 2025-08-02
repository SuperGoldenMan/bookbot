import sys

letter = sys.argv[1]
number = int(sys.argv[2])

def main(letter):
    if len(sys.argv) != 3:
        print("Usage: python3 main.py letter number")
        sys.exit(1)
    i = 0
    letters = []
    while i < number:
         letters.append(letter)
         i += 1
    print("".join(letters))

main(letter)