import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = get_num_words(book)
    print(f"Found {word_count} total words")
    symbol_count = symbol_counter(book)
    sorted_list = list_dict(symbol_count)
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

from stats import get_num_words, get_book_text, symbol_counter, list_dict, sort_on



main()