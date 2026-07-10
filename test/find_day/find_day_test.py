from src.find_day.util import find_day

def test_find_day_standard():
    assert find_day(8, 5, 2015) == "WEDNESDAY"

def test_find_day_leap_year():
    assert find_day(2, 29, 2024) == "THURSDAY"

def test_find_day_new_year():
    assert find_day(1, 1, 2050) == "SATURDAY"