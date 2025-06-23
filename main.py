from stats import get_number_words
from stats import get_number_char
from stats import sort_dict
import sys
def main():
    if (len(sys.argv) != 2):#if our input command to the program doesnt have two arguments for program and filepath
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book = sys.argv[1] #using the second element of the sys.argv list which should be the book path
    book_text = get_book_text(book)
    print("============ BOOKBOT ============\n----------- Word Count ----------\n")
    get_number_words(book_text)
    print("--------- Character Count -------\n")
    character_count = get_number_char(book_text)
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