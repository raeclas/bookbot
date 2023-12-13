def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    num_words = word_counter(text)
    num_chars = char_counter(text)
    num_chars_sorted_list = sort_char_list(num_chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in num_chars_sorted_list:
        if item["char"].isalpha() == False:
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

    

def open_book(path):
    with open(path) as f:
        return f.read()
    
def word_counter(text):
    words = text.split()
    return len(words)

def char_counter(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def sort_char_list(num_chars):
    sorted_list = []
    for key in num_chars:
        sorted_list.append({"char":key,"num":num_chars[key]})
    sorted_list.sort(reverse=True, key = sort_on)
    return sorted_list


main()
