def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def symbol_counter(book_text):
    char_count = {}
    book_text_lower = book_text.lower()
    for letter in book_text_lower:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

def list_dict(char_count):
    list_of_dicts = []
    for char, count in char_count.items():
        new_dict = {"char": char, "count": count}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(dict):
    return dict["count"]
    