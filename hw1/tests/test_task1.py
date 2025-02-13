import pytest
import parentDir
import task1

# verify output of print statement
def test_task1(capsys):
    task1.hello()

    assert capsys.readouterr().out == "Hello, World!\n"