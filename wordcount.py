# put your code here.
import sys
from collections import Counter

def word_counter(filename):
    """ Counts number of times word appears in given input file """

    input_file = open(filename)

    word_count_list = []

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
            word_count_list.append(word)
           
    final_output = Counter(word_count_list)

    # for key, value in word_count_dict.iteritems():
    #     print key, value   

    # result = sorted([(k, v) for k, v in word_count_dict.items()])

    # print final_output

    for thing in final_output:
        print thing, final_output[thing]

    input_file.close()



word_counter(sys.argv[1])