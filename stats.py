def get_book_text(filepath):
    with open(filepath) as f:
     return f.read()

def parse_book_text(text):
    split_text = text.split()
    return len(split_text)

def count_symbols(text):
    symbols = {}
    for c in text:
        lwr = c.lower()
        if lwr not in symbols:
            symbols[lwr] = 0
        symbols[lwr] += 1
    return symbols

def sort_symbols(symbols):
    sorted_symbols = sorted(symbols.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_symbols:
        if char.isalpha():
            print(f"{char}: {count}")