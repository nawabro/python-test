import pytest
from app import add  # replace 'app' with the name of your file without the .py

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0