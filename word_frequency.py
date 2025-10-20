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

def get_sentence():
    user_sentence = input("Enter a sentence: ")
    while not is_sentence(user_sentence):
        print("This does not meet the criteria for a sentence (Must start with a capital letter and end with .!?).")
        user_sentence = input("Enter a valid sentence: ")
    return user_sentence

def wordlist(sentence, unique_words, frequencies):
    lower_sentence = sentence.lower()
    cleaned_sentence = re.sub(r"[^\w\s']"," ", lower_sentence)
    all_words = cleaned_sentence.split()
    for word in all_words:
        word = word.strip("'")
        if not word:
            continue
        if word in unique_words:
            i = unique_words.index(word)
            frequencies[i] += 1
        else:
            unique_words.append(word)
            frequencies.append(1)

def results(unique_words, frequencies):
    print("\n Word Frequency Results ")
    #AI zip function combines two lists into a list of 
    if unique_words:
        for word, count in zip(unique_words, frequencies):
            print(f"{word} : {count}")
    else:
        print("No words found")

unique_words = []
frequencies = []
user_sentence = get_sentence()
wordlist(user_sentence, unique_words, frequencies)
results(unique_words, frequencies)
