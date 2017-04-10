# put your code here.
import sys
from collections import Counter

def word_counter(filename):
    """ Counts number of times word appears in given input file """

    input_file = open(filename)

    word_count_dict = {}

    for line in input_file:
        line = line.rstrip().split(" ")
        for word in line:
            word = word.lower()
            if len(word) != 0:
                while not word[0].isalpha():
                    word = word[1:]
                    if len(word) == 0:
                        break
                if len(word) != 0:
                    while not word[-1].isalpha():
                        word = word[:-1]
                        if len(word) == 0:
                            break
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    # for key, value in word_count_dict.iteritems():
    #     print key, value   

    result = sorted(word_count_dict.items())

    for word, count in result:
        print word, count

    input_file.close()

word_counter(sys.argv[1])