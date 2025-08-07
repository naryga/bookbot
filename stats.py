def get_num_words(str_of_wrds):
    words = str_of_wrds.split()
    return len(words)

def count_char_instances(str_of_chars):
    str_of_chars = str_of_chars.lower()
    char_counts = {}
    for char in str_of_chars:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    
    return char_counts
