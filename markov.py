"""Generate Markov text from text files."""

from random import choice

import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    return contents

    # your code goes here

    return "Contents of your file as one long string"


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    text_lst = text_string.split()
    


    chains = {}
    for i in range(len(text_lst)-n):
        tup_n = tuple(text_lst[i:i+n])
        val = text_lst[i+n]
        if tup_n in chains:
            chains[tup_n].append(val)
        elif tup_n not in chains:
            chains[tup_n] = [val]  
           


    # your code goes here

#    print(chains)

    return chains


def make_text(chains, n):
    """Return text from chains."""

    n_gram = choice(list(chains.keys()))
    words = list(n_gram)
    # print(words)

    while n_gram in chains:
        next_word = choice(chains[n_gram])
        words.append(next_word)
        n_gram = tuple(n_gram[-(n-1):]) + (next_word,)
        # print(n_gram)
        # print(next_word)
    # your code goes here

    return " ".join(words)


input_path = sys.argv[1]
input_ngram = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, input_ngram)

# Produce random text
random_text = make_text(chains, input_ngram)

print(random_text)
