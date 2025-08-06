from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    filepath = sys.argv[1] 
    book_text = get_book_text(filepath)

    num_words = parse_book_text(book_text)
    # print(f'{num_words} words found in the document')

    count_symbols_result = count_symbols(book_text)
    # print(f'Symbols count: {count_symbols_result}')



    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    sort_symbols(count_symbols_result)
    print('============= END ===============')



if __name__ == "__main__":
    main()