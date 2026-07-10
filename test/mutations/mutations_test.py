from src.mutations.util import mutate_string

def test_mutate_string_standard():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"

def test_mutate_string_first_character():
    assert mutate_string("hello", 0, "H") == "Hello"

def test_mutate_string_last_character():
    assert mutate_string("python", 5, "N") == "pythoN"

def test_mutate_string_numeric_character():
    assert mutate_string("word", 2, "3") == "wo3d"