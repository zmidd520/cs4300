def count_words(file):
    # read file contents
    content = file.read().split()

    # get word count and return it
    numWords = len(content)

    return numWords


    