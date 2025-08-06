def get_book_text(filepath):
    with open(filepath) as f:
     return f.read()

def parse_book_text(text):
    split_text = text.split()
    return len(split_text)

def count_symbols(text):
    symbols = {}
    for c in text:
        c = c.lower()
        if c not in symbols:
            symbols[c] = 0
        symbols[c] += 1
    return symbols

def sort_symbols(symbols):
    sorted_symbols = sorted(symbols.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_symbols:
        if char.isalpha():
            print(f"{char}: {count}")