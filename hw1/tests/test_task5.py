import pytest
import parentDir
import task5


def test_threeBooks(capsys):
    task5.threeBooks()

    assert capsys.readouterr().out == "[\'The Maze Runner - James Dashner\', \'The Hunger Games - Suzanne Collins\', \"Ranger's Apprentice - John Flanagan\"]\n"

def test_dict():
    assert len(task5.students) == 5

    # test that key-value pairs line up correctly
    assert task5.students[123123] == "John Smith"
    assert task5.students[112233] == "Craig Thomas"
    assert task5.students[111111] == "Nancy Jones"
    assert task5.students[101010]  == "Samuel Jackson"
    assert task5.students[999999] == "Savannah Peterson"
