import random
import text_stats
from typing import List, Dict
import sys

with open(sys.argv[1], "r", encoding="utf8") as file: #Read the first argument as a file
    text = file.read() #Get the text from the filed 
    list_of_words :List = text_stats.seperate_words(text) #Split the textfile into list of words
    cur_word= sys.argv[2] #Store the second argument
    msg = cur_word 
    counter_words = 0
    #Get the following words dictionary from text_stats.
    following_words :Dict = text_stats.count_following_words(list_of_words)

    #until there are no successors of cur_word, or the maximum number of words has been picked
while((counter_words <= int(sys.argv[3])) and (len(following_words[cur_word].keys()) > 0)):
    #Chose a random word with weights corresponding to the probability - Behaves as set, therefore requires list and [0] to get 
    #a string.
    cur_word = random.choices(list(following_words[cur_word].keys()), weights=list(following_words[cur_word].values()))[0]
    #Append the new word in the msg string
    msg = msg + " " + cur_word
    counter_words += 1
print(msg)