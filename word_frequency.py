#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def wordlist():
    lower_sentence = user_sentence.lower()
    cleaned_sentence = re.sub(r'[^\w\s]',' ', lower_sentence)
    all_words = cleaned_sentence.split()
    word = 0
    for word in all_words:
        if word in unique_words:
        # If the word is already in the unique list, increment its count 
            i = unique_words.index(word)
            frequencies[i] += 1
        else:
        # If it's a new word, add it to the unique list and set its initial frequency to 1
            unique_words.append(word)
            frequencies.append(1)
def results():
    print("\n Word Frequency Results ")
    # Only print results if words were actually found

    #Took this from Gemeni AI
    if unique_words:
        for word, count in zip(unique_words, frequencies):
            print(f"{word} : {count}")
    else:
        print("No words found ") 

# validation loop
user_sentence = input("Enter a sentence: ")
while is_sentence(user_sentence) == False:
    print("This does not meet the criteria for a sentence (Must start with a capital letter and end with .!?).")
    user_sentence = input("Enter a valid sentence: ")

unique_words = []
frequencies = []
wordlist()
results()
