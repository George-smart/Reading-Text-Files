# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string

# Removing punctuation marks
def strip_punctuations(line) :
    for charater in string.punctuation:
        line = line.replace(charater, "")
    return line

def read_file_content(filename):
    # [assignment] Add your code here 
    # read file 
    file = open(filename, 'r')
    return file.read()
    file.close()

word_count = {}

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    new_text = strip_punctuations(text)

    words = new_text.split()
    # for each word in words
    for word in words:
        # Convert the word into lower case
        word = word.lower()
        # print(words)
        # And check if it is not in our dictionary
        if word not in word_count:
            # If not, create a new entery for it
            word_count[word] = 0
            # Then increment its counter by 1
        word_count[word] += 1
   
    # Traverse the ten words and print their count
    ten_words = list(word_count.keys())
    for word in ten_words:
        # word must take a minimal of 15 spaces; count can take minimum of 8
        print("{0:15}{1:8}".format(word, word_count[word]))


count_word = count_words()
print(count_word)