import pytest
import parentDir
import task2

def test_task2():
    assert type(task2.task2_int) == int
    assert type(task2.task2_float) == float
    assert type(task2.task2_str) == str
    assert type(task2.task2_bool) == bool