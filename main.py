import sys
from stats import count_words_in_str, count_char_occur, form_sorted_list_of_dicts, write_report

def get_book_text(filepath: str):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(filepath: str):
    book_text = get_book_text(filepath)
    num_words = count_words_in_str(book_text)
    char_dict = count_char_occur(book_text)
    sorted_list_of_dicts = form_sorted_list_of_dicts(char_dict)
    write_report(filepath, num_words, sorted_list_of_dicts)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])

