def count_words(filename):
    with open(filename, 'r') as f:
        content = f.read().split()

        # get length of lines
        numWords = len(content)

    return numWords

#words = count_words("task6_read_me.txt")
#print(words)

    