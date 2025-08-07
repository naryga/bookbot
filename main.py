from stats import get_num_words
from stats import count_char_instances

def get_book_text(path_to_file):
    
    # open the `path_to_file` and save it to `file_contents`
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    txt = get_book_text('./books/frankenstein.txt')
    num_words = get_num_words(txt)
    num_chars = count_char_instances(txt)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()