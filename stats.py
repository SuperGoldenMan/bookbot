def num_words(text):
    return len(text.split())

def char_counts(text):
    counts = {}
    for char in text:
        char_lower = char.lower()
        counts[char_lower] = counts.get(char_lower, 0) + 1
    return counts

def sorted_char_counts(text):
    counts = char_counts(text)
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts