import pytest
import parentDir
import task7
import requests

def test_good_req():
    assert task7.r.status_code == 200
    assert "<!doctype html>" in task7.r.text   # make sure returned text is HTML

def test_bad_req():
    assert task7.fakeR.status_code == 404
    assert "<!doctype html>" in task7.r.text   # make sure returned text is HTML
