from src.iterables_and_iterators.util import calculate_probability

def test_calculate_probability():
    letters = ["a", "a", "c", "d"]
    k = 2
    
    assert calculate_probability(letters, k) == "0.8333"