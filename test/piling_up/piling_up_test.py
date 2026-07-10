from src.piling_up.util import check_stackability

def test_check_stackability_yes():
    blocks = [4, 3, 2, 1, 3, 4]
    assert check_stackability(blocks) == "Yes"

def test_check_stackability_no():
    blocks = [1, 3, 2]
    assert check_stackability(blocks) == "No"