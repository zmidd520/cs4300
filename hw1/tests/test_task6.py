import pytest
import parentDir
import task6
import os

# create function based on filename
def create_function(file, wordCount):
    name = file[:-4]

    # create dynamic test function 
    exec(f"""def test_{name}():      
    with open(\"{file}\", 'r') as f:       
        words = task6.count_words(f)
        assert words == {wordCount}
    """)

    return locals()[f"test_{name}"]

def test_task6():
    for file in os.listdir():
        if ".txt" in file:

            # get the word count for the file locally
            with open(file, 'r') as f:
                wcount = len(f.read().split())

            # generate and call dynamic function
            func = create_function(file, wcount)
            func()

test_task6()