"""Generate Markov text from text files."""

from random import choice
import twitter

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    new_file = open(file_path)
    read_file = new_file.read()

    new_file.close()
     

    return read_file


def make_chains(text_string):
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

    chains = {}
    words = text_string.split() 

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = [words[i + 2]]

        if key not in chains:
            chains[key] = value
        else:
            chains[key].append(words[i + 2])
        


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    key = choice(chains.keys())
    random_value = choice(chains[key])

    words.extend(key)
    words.append(random_value)
    print words

    while True:
        #print random_key
        if key not in chains:
            break
        else:
            random_value = choice(chains[key])
            key = (key[1], random_value)
            words.append(random_value)
    
    while True:
        if len(" ".join(words)) < 140:
            return " ".join(words)
        else:
            words.pop()           


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print chains

# Produce random text
random_text = make_text(chains)

print random_text
