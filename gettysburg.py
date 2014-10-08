#!/usr/bin/python3

'''Gettysburg Address

This is an exercise in file analysis. Fundamentally it is an exercise in the use of the basic collection objects in
Python such as strings, lists, tuples, dictionaries and sets.request

We are going to use Abraham Lincoln's Gettysburg address of 1863, This is famous for many things, including being a
short speech.

We are going to do some simple analysis on this.
1. Count the number of words in the speech. We will exclude from our analysis a number of 'stop words', in our example
these will be the definite and indefinite articles and some personal pronouns.
2. Count the unique words in the collection produced by 1 above.
3. Count the number of occurrences of each word.

Some hints
1. Import the string module. This gives string.whitespace, a string containing all of the whitespace characters
and string.punctuation, a string containing all of the punctuation characters.

'''

# Import:
# string (gives us whitespace and punctuation lists)
# urllib.request (so that we can read from the net)
# URLError (in case we have net-related problems
import string
import urllib.request
from urllib.error import URLError

# Variables to hold file URLs
SPEECH_URL = "http://mf2.dit.ie/gettysburg.txt"
STOPWORDS_URL = "http://mf2.dit.ie/stopwords.txt"

def makeWordList(gFile, stopWords):
    """Create a list of words from the file while excluding stop words."""
    speech = []                                     # list of speech words: initialized to be empty

    for lineString in gFile:
        lineList = lineString.strip(string.whitespace).split()               # split each line into a list of words and strip whitespace
        for word in lineList:
            word = word.lower()                     # make words lower case (we consider a word in lowercase and uppercase to be equivalent)
            word = word.strip(string.punctuation)   # strip off punctuation
            if (word not in stopWords) and (word not in string.punctuation):
                # if the word is not in the stop word list, add the word to the speech list
                speech.append(word)
    return speech

def countWords(speech):
    """Create a dictionary and count the occurrences of each word.
    If a word already exists in the dictionary, add 1 to its counter
    otherwise set a counter for to to an initial value of 1"""
    counts = {}
    for word in speech:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def main():
    '''Process the speech once you can successfully open both the speech and the stop words files from the net.'''
    try:
        #Open the speech and stop words files from the net
        local_filename, headers = urllib.request.urlretrieve(SPEECH_URL)
        gFile = open(local_filename, "r")
        local_filename, headers = urllib.request.urlretrieve(STOPWORDS_URL)
        stopFile = open(local_filename, "r")

        #Make a tuple of all the stop words while losing the newline char
        stopWords = tuple(stopFile.read().strip().split(','))
        # Close the stop words file as we don't need it any more
        stopFile.close()

        # Make word list from speech while excluding stop words
        speech = makeWordList(gFile, stopWords)
        # Make a set of words from speech which automatically assures that each entry is unique
        unique = set(word for word in speech)

        # Close the speech file as we don't need this any more
        gFile.close()

        # Print the results
        print("Speech Length: {}".format(len(speech)))
        print("Unique words: {}".format(len(unique)))
        print("\nWord count")

        words = countWords(speech)

        for word in words:
            print("{}: {}".format(word, words[word]), end=" ")
        print("\n")

    except IOError as e:
        print("I/O Error: {}".format(e))
    except URLError as u:
        print("URL Error: {}".format(u))

# Run if stand-alone
if __name__ == '__main__':
    main()
