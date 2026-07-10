from src.merge_the_tools.util import merge_the_tools

def test_merge_the_tools_standard(capsys):
    merge_the_tools('AABCAAADA', 3)
    captured = capsys.readouterr()
    assert captured.out == "AB\nCA\nAD\n"

def test_merge_the_tools_all_same(capsys):
    merge_the_tools('AAAAAA', 2)
    captured = capsys.readouterr()
    assert captured.out == "A\nA\nA\n"

def test_merge_the_tools_no_duplicates(capsys):
    merge_the_tools('ABCDEF', 3)
    captured = capsys.readouterr()
    assert captured.out == "ABC\nDEF\n"

def test_merge_the_tools_single_chunk(capsys):
    merge_the_tools('AABBCC', 6)
    captured = capsys.readouterr()
    assert captured.out == "ABC\n"