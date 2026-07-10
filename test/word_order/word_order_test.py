from src.word_order.util import get_word_order

def test_get_word_order():
    words = [
        "bcdef",
        "abcdefg",
        "bcde",
        "bcdef"
    ]
    
    expected_output = "3\n2 1 1"
    assert get_word_order(words) == expected_output