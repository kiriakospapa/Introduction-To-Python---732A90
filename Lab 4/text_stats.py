#Additional Questions
#In what way did you "clean up" or divide up the text into words (in the program; the text files should be left
#unaffected)? This does not have to be perfect in any sense, but it should at least avoid counting "lord",
#"Lord" and "lord." as different words.

#Answer: It can be seen in the function seperate_words, moreover it filters the list to only include those that match 
# a specific pattern. Then lowercasing the remaining words and removing any wrong characters with _replace_incorrect_characters() function.
#For uppercase, the lowercase converts the word. The additional functions as filtering to have a specific patter or
#the function _replace_incorrect_characters() is used to convert for example lord. to only word ord so it counts as one.

#Which data structures have you used (such as lists, tuples, dictionaries, sets, ...)? Why does that choice
#make sense? You do not have to do any extensive research on the topics, or try to find exotic modern data
#structures, but you should reflect on which of the standard data types (or variants thereof) make sense. If
#you have tried some other solution and updated your code later on, feel free to discuss the effects!

#Answer: Depending on the question, we have used lists, dictionaries and tuples. The dictionaries are ideal to store
#the word as key, and number of occurences as values.
# We have used list to store all the words that are in the text, maybe using tuples would be more memory efficient and
# speed efficient

#Import libraries
import sys
import re
from typing import List, Dict
from collections import Counter
TO_REPLACE = ["`","\\","'",",",".",";","?","!",":","-","—","[","]","_"] #Replace all  /, ' ¨

def main(args):
    try:
        with open(args[1], "r", encoding="utf8") as file: #Read the first argument as a file
            text = file.read() #Get the text from the filed  
            frequency_of_letters :Dict = count_letters(text)
            print_letter_occurance(frequency_of_letters)
            
            list_of_words :List = seperate_words(text)
            print_number_of_words_and_unique_words(Counter(list_of_words))
            
            following_words :Dict = count_following_words(list_of_words)
            print_following_words(Counter(list_of_words), following_words)
            
            if len(args) == 3: #If 3 arguments are given
                with open(args[2], "w", encoding="utf8") as new_file: #Open and write as new_file.
                    #Stores the output in new_file
                    print_letter_occurance(frequency_of_letters, new_file)
                    print_number_of_words_and_unique_words(Counter(list_of_words), new_file)
                    print_following_words(Counter(list_of_words), following_words, new_file)
    except FileNotFoundError as e: #If no arguments are provided.
        raise FileNotFoundError("The file does not exist!")
    file.close()

def print_letter_occurance(letters: Counter, write_file=None): #write_file is an optional argument if we want to store it in a file.
    '''Prints each letter and their number of occurences.'''
    print("\n".join([f"{i[0]}: {i[1]}"for i in letters]), file=write_file)#List comprehension where each key and value is printed and separated by a newline.  

def print_number_of_words_and_unique_words(words: Counter, write_file=None):#write_file is an optional argument if we want to store it in a file.
    '''Prints number of words and number of unique words. '''
    print(f"The text contains {sum(words.values())} words and {len(words)} unique words", file=write_file) #Prints the sumf of the values and the length of the input.
    
def print_following_words(matched_words: Counter, following_words: Dict, write_file=None):#write_file is an optional argument if we want to store it in a file.
    '''Prints the most common word and number occurences.
    Print the most common following words and number of occurences.'''
    for i in matched_words.most_common(5): # Iterate over the 5 most common words
        print(f"{i[0]} ({i[1]} occurrences)", file=write_file) #Print the word and number occurences
        print("\n".join([f"-- {j[0]}, {j[1]}" for j in following_words[i[0]].most_common(3)]), file=write_file)#For each most common word,
        #print the 3 most common following words

def count_letters(text: str): #-> Dict
    '''Count the occurrences of each letter in a given string
    Returns key-value pairs in a tuple??'''
    return(Counter([i.lower() for i in text if i.isalpha()]).items()) #List comprehension converts all letters to lowercase and 
    #filters non-alphabetic letters. Thereafter each word is counted by Counther function and retunred as key-value pairs in a tuple. 

def seperate_words(text: str): # -> List[str]
    '''This part of code splits the text into words and regex pattern matches every word, 
    if a word matches it replaces extra characthers that can appear when it was split. 
    Thereafter, it returns a list of words.'''
    def _replace_incorrect_characters(chars: List[str], word: str):
        '''Replace special characters in each word, if the character is in TO_REPLACE list'''
        for char in chars: #For each element in chars, replace it, if it exists in the word.
            word = word.replace(char,"") 
        return word
    #Splits an input text into a list of words, thereafter it filters the list to only include those that match a specific pattern.
    # Then lowercasing the remaining words and removing any wrong characters with _replace_incorrect_characters function.
    return [_replace_incorrect_characters(TO_REPLACE, word.lower()) for word in text.split() if re.search("^[,.;?!:-—\[\]_]?[A-Za-z-´`'’]+[,.;?!:-—\[\]_]?$", word.strip())]

def count_following_words(matched_words: List[str]) : #-> Dict
    '''Counts following words in a given list of words. Thereafter, stores them in a dictionary where the keys are the first word 
    of the pair and the values are Counter objects that store the frequency of the following word.'''
    dct = {} #Create empty dictionary
    for idx in range(len(matched_words) - 1): # Iterate over each index from first to second last.
        if matched_words[idx] not in dct: #Check if word is not in dictionary
            dct[matched_words[idx]] = Counter()
            #Then creates an empty counter object (To create a new counter dictionary for following word)
        dct[matched_words[idx]][matched_words[idx + 1]] += 1 #Increases the value of the following word
    return dct

if __name__ == "__main__":
    if len(sys.argv) <= 1:  #Check if argument for file name is given, else raise FileNotFoundError message
        raise FileNotFoundError("No argument for file name found.")
    main(sys.argv)
    