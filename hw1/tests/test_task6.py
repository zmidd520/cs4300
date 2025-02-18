import pytest
import parentDir
import task6
import os

# create function based on filename
def create_function(name):

    # create dynamic test function 
    exec(f"""def test_{name}(filename):
    words = task6.count_words(filename)
    assert words == len(filename.read().split())
    """)

    return locals()[f"test_{name}"]
"""
def test_task6():
    for file in os.listdir():
        if ".txt" in file:
            name = file[:-4]
            func = create_function(name)
            func(file)
"""