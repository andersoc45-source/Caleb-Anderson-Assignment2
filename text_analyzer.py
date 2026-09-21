# text_analyzer.py
# Caleb Anderson

# Reads the file 
# Returns a list of words
def read_file(file_name):
# Open the file and copy its contents to a list
    with open(file_name, 'r') as the_file:
        the_text_content = the_file.read()
    
    my_list = the_text_content.lower().split()

    return my_list

# Retrns a dictionary of word counts
def find_word_count(my_list):
    # Let's count the occurrences of each word.
    word_count_dict = {word: my_list.count(word) for word in my_list}

    return word_count_dict

# Returns a list of long words
def find_long_words(my_list):
    # Now let's find the words with more than 3 characters.
    long_words = [word_element for word_element in my_list if len(word_element) > 3]
                
    return long_words

# Prints analysis info of word list
def print_word_info(my_list, word_count_dict, long_words):
    print(f"The total number of words is: {str(len(my_list))}")
    print(f"The unique words count is: {str(len(word_count_dict))}")
    print(f"The most frequent words are:")
    
    for word, count in sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"'{word}': {count}")
    
    print(f"Long words (more than 3 characters): {str(len(long_words))}")

# You will need to create a text file named 'sample.txt' for testing.
file_contents = read_file("sample.txt")
file_word_count = find_word_count(file_contents)
file_long_words = find_long_words(file_contents)

print_word_info(file_contents, file_word_count, file_long_words)