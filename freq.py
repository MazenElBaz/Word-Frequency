# --------------------------
# Name: Mazen ElBaz
# Date: Sept. 2018
# Exercise 3:Word Frequency
# --------------------------

import sys

uniqueWords = {}


def errorHandle(commLineArgumentsList):

    """ Checks to see if the user entered the required number of command
    line arguments. If the user did not, it prints that there are too few/
    many command line arguments and demonstrates the correct usage of the
    program. It then immediately exits the program.

    Argument:
    commLineArgumentsList: a list of all the command-line arguments entered
    by the user.

    Returns:
    None (but prints an error message to standard output) """

    # Since the user should only input two command-line arguments(the .py
    # file and the input file name), any additional or missing arguments
    # will print an error to the user
    if len(commLineArgumentsList) < 2:

        print("There are too few command-line arguments \nAn input file" +
              " name is missing \nAfter freq.py please type an input" +
              " file name that contains plain text only \nIt should be" +
              " in the following format: 'python3 freq.py" +
              " <input_file_name>'")

        sys.exit(1)

    elif len(commLineArgumentsList) > 2:

        print("There are too many command-line arguments \nAfter" +
              " freq.py, only one input file name is required \nIt" +
              " should be in the following format: 'python3 freq.py" +
              " <input_file_name>'")

        sys.exit(1)


def openFile(fileName):

    """ Takes in the name of a file and opens that file in read mode, and
    returns a file object.

    Argument:
    fileName: the name of a file

    Returns:
    file: the file object which will allow the program to read/analyze the
    opened file. """

    # opens sys.argv[1](fileName) in read mode and stores the file object
    # in the variable file
    file = open(fileName, "r")

    return(file)


def readFile(filePointer):

    """ Takes in the file object and reads every line in the opened file
    and stores it in a list. Then, for every line, it strips all whitespace
    characters and stores the modified lines in a second list.

    Argument:
    filePointer: the file object which will allow the function readFile to
    read the lines in the opened file

    Returns:
    strippedLinesList: a list of the lines read from the opened file with
    all the whitespace characters removed """

    linesList = filePointer.readlines()
    filePointer.close()
    # strip() is used to remove whitespace characters found in any line
    # stored in the list linesList
    strippedLinesList = [line.strip() for line in linesList]

    return(strippedLinesList)


def wordCount(fileLinesList):

    """ Takes in a list of the lines read from the opened file. For every
    line in the list, it splits the line into a list of words, and then
    checks to see if the words are unique(not in the dictionary uniqueWords)
    or not. If they are unique, it addes them to the dictionary and assigns
    a value of 1(word count). If they are not unique, it increments their
    value by 1.

    Argument:
    fileLinesList: a list of the lines read from the opened file

    Returns:
    None """

    wordsList = []

    for line in fileLinesList:

        wordsList = line.split()

        for word in wordsList:

            if word not in uniqueWords:
                uniqueWords[word] = 1
            else:
                uniqueWords[word] = uniqueWords[word] + 1
    return None


def wordsFrequency():

    """ Sorts all the keys(unique words) in the dictionary uniqueWords in
    lexicographic order. It then counts the total number of words found in
    the text. Finally, it iterates through a list of tuples to calculate the
    frequency of each unique word, and adds the new information(frequency)
    to the key in the dictionary it was calculating the frequency for.

    Argument:
    None

    Returns:
    None """

    wordsInfo = []
    totalWords = 0
    count = 0
    frequency = 0

    wordsInfo = sorted(list(uniqueWords.items()))
    # c represents the count of every unique word in the dictionary.
    # To find the total number of words in the text, all the counts of all
    # unique words have to be added
    for w, c in wordsInfo:
        totalWords = totalWords + c

    for i in range(0, len(wordsInfo)):

        count = wordsInfo[i][1]
        frequency = round(count/totalWords, 3)
        # .update() assigns one more value(frequency) to
        # every key(unique word) in the dictionary
        uniqueWords.update({wordsInfo[i][0]:
                            (wordsInfo[i][1], frequency)})

    return None


def writeFrequencyTable(writeFile):

    """ Sorts and takes all the items(keys and their values) in the
    dictionary uniqueWords and stores them in a list. It then iterates
    through the list and writes a frequency table to a file

    Argument:
    writeFile: the input file name enterted by the user, which will be used
    to generate the name of the output file

    Returns:
    None (but writes a frequency table with all the unique words and their
    counts and frequencies to an output file """

    completeWordsInfo = []

    completeWordsInfo = sorted(list(uniqueWords.items()))

    outputFile = open((writeFile + '.out'), 'w')

    for i in range(0, len(completeWordsInfo)):

        frequencyLine = completeWordsInfo[i][0] + ' ' \
            + str(completeWordsInfo[i][1][0]) + ' ' \
            + str(completeWordsInfo[i][1][1]) + '\n'

        outputFile.write(frequencyLine)

    outputFile.close()

    return None


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.

    # all the functions are called in main() in the correct order
    errorHandle(sys.argv)
    fileObject = openFile(sys.argv[1])
    lines = readFile(fileObject)
    wordCount(lines)
    wordsFrequency()
    writeFrequencyTable(sys.argv[1])
