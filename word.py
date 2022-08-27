
import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    WORDLIST_FILENAME="/home/think-pad/Desktop/hangman.py/words.txt"
    print("Loading word list from file...")
    f = open(WORDLIST_FILENAME, 'r')
    line = f.readline()
    word_list = line.split()
    print(len(word_list), "words loaded.\n")
    # word_list = ["navgurukul", "learning", "kindness"]
    return word_list

def choose_word():
    
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word

