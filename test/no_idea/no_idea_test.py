from src.no_idea.util import calculate_happiness

def test_calculate_happiness():
    arr = ["1", "5", "3"]
    set_a = {"3", "1"}
    set_b = {"5", "7"}
    
    assert calculate_happiness(arr, set_a, set_b) == "1"