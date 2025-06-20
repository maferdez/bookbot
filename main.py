from stats import get_number_words
from stats import get_number_char
def main():
    book = get_book_text("/home/mafer/bootdevProjects/bookbot/books/frankenstein.txt")
    get_number_words(book)
    character_count = get_number_char(book)
    print(character_count)
def get_book_text(filepath):
    #this function takes a filepath as input and returns the contents of the file as a string
    with open(filepath) as file:
        book_text = file.read()
    return book_text

main()