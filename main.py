import sys
from stats import get_num_words
from stats import count_char_instances
from stats import formated_chars

def get_book_text(path_to_file):
    
    # open the `path_to_file` and save it to `file_contents`
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def pretty_report(book_file, num_words, num_chars):
    # formated report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in num_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

def main():
    # must have at least 2 arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_file = sys.argv[1]
    txt = get_book_text(book_file)
    num_words = get_num_words(txt)
    num_chars = count_char_instances(txt)
    num_chars = formated_chars(num_chars)

    pretty_report(book_file, num_words, num_chars)

main()