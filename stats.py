def get_number_words(book_text):
    #this function takes text from a book as a string type
    #and returns the number of words in the book

    book_text_list = book_text.split() #split will take our string and split it into list of the words based off the spacing
    number_words = len(book_text_list) #the range of the list should be the total number of words
    
    print(f"Found {number_words} total words\n")
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

def sort_on(items):#this function defines the key to sort on using the .sort() method. It takes in a items obj of type dict and returns the desired key
    return items["num"]

def sort_dict(char_dict):
    #this functions takes a dictionary of char's and their counts and
    #returns a sorted list of dictionaries based on count
    #the list has structure {"char":"x", "num": y} where x is the char as a str and y is the count as an int
    #the list of dictionaries is sorted by count from greatest to least

    #first we must take our original dictionary and build the new list of dictionaries from it

    list_char_dict = []
    
    for char_key in char_dict:
        temp_small_dict = {"char": char_key, "num": char_dict[char_key]}
        list_char_dict.append(temp_small_dict)
        list_char_dict.sort(reverse=True, key=sort_on)
    return list_char_dict