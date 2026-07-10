from src.find_runner_up.util import find_runner_up

def test_find_runner_up_standard(capsys):
    scores = [2, 3, 6, 6, 5]
    find_runner_up(scores)
    captured = capsys.readouterr()
    assert captured.out.strip() == "The runner-up score is 5"

def test_find_runner_up_negative_numbers(capsys):
    scores = [-10, -20, -30, -10]
    find_runner_up(scores)
    captured = capsys.readouterr()
    assert captured.out.strip() == "The runner-up score is -20"

def test_find_runner_up_sequential(capsys):
    scores = [10, 9, 8, 7]
    find_runner_up(scores)
    captured = capsys.readouterr()
    assert captured.out.strip() == "The runner-up score is 9"