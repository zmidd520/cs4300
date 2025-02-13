import pytest
import parentDir
import task3

def test_checkNum(capsys):
    task3.checkNum(5)
    assert capsys.readouterr().out == "num is positive\n"

    task3.checkNum(-5)
    assert capsys.readouterr().out == "num is negative\n"

    task3.checkNum(0)
    assert capsys.readouterr().out == "num is zero\n"

def test_primes(capsys):
    task3.primes()
    assert capsys.readouterr().out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

def test_sum(capsys):
    task3.sum()
    assert capsys.readouterr().out == "Sum (1 to 100): 5050\n"