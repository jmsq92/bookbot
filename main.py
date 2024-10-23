def main():

#Initialize each function.
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    report = char_report(char_dict)

#Returns text to console.
def  get_book_text(path):
    with open(path) as f:
        return f.read()            

#Returns number of words.
def get_num_words(text):
    words = text.split()
    return len(words)

#Returns dictionary with count of each character.
def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#Print report to console.
def char_report(dictionary):
    conver_to_list = list(dictionary.items()) #.items() used to extrac dictionary pairs. list() used to conver tu tuple.
    conver_to_list.sort()
    
    for character, count in conver_to_list: #referencia indirecta a los contenidos de cada tupla.
        if character.isalpha():
            print(f"The '{character}' character was found {count} times")

    print("--- End Report ---")

main()