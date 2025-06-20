def get_number_words(book_text):
    #this function takes text from a book as a string type
    #and returns the number of words in the book

    book_text_list = book_text.split() #split will take our string and split it into list of the words based off the spacing
    number_words = len(book_text_list) #the range of the list should be the total number of words
    
    print(f"{number_words} words found in the document")
    return 0

def get_number_char(book_text):
    #this function takes in a book as type string and
    #returns the number of times each char appears (including symbols and spaces)
    #it does not distinguish between capital and lowercase char's

    #to do this we can loop over the entire book string and add each character as key:value pair in a dict

    #creating the dictionary
    char_dict = {}

    for char in book_text:
        lowercase_char = char.lower()
        if lowercase_char in char_dict: #if the key already exists in the dictionary
            char_dict[lowercase_char] += 1 #increment the value at the key by 1
        else:
            char_dict[lowercase_char] = 1 #if it doesn't exist yet add the key as the char and a value of 1 to start the count
    return char_dict