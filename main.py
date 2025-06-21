from stats import get_number_words
from stats import get_number_char
from stats import sort_dict
def main():
    book = get_book_text("/home/mafer/bootdevProjects/bookbot/books/frankenstein.txt")
    print("============ BOOKBOT ============\n----------- Word Count ----------\n")
    get_number_words(book)
    print("--------- Character Count -------\n")
    character_count = get_number_char(book)
    sorted_dictionary_list = sort_dict(character_count)
    for i in range(0,len(sorted_dictionary_list)):
        if (sorted_dictionary_list[i]["char"].isalpha()):
            print(f"{sorted_dictionary_list[i]["char"]}: {sorted_dictionary_list[i]["num"]}")
    print("============= END ===============")    
        
def get_book_text(filepath):
    #this function takes a filepath as input and returns the contents of the file as a string
    with open(filepath) as file:
        book_text = file.read()
    return book_text

main()