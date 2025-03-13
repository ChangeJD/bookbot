def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def num_words(book_text):
    words = book_text.split()
    word_counter = 0
    for word in words:
        word_counter += 1
    return word_counter



def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = num_words(book)
    print(f"{word_count} words found in the document")


main()