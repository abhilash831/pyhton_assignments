from src.list_operations.util import perform_operation

def test_perform_operation_append_and_print(capsys):
    arr = []
    perform_operation(arr, ["append", "5"])
    perform_operation(arr, ["print"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "[5]"
    assert arr == [5]

def test_perform_operation_insert_and_sort():
    arr = [3, 1]
    perform_operation(arr, ["insert", "1", "2"])
    perform_operation(arr, ["sort"])
    assert arr == [1, 2, 3]

def test_perform_operation_remove_and_pop():
    arr = [10, 20, 30]
    perform_operation(arr, ["remove", "20"])
    perform_operation(arr, ["pop"])
    assert arr == [10]

def test_perform_operation_reverse():
    arr = [1, 2, 3, 4]
    perform_operation(arr, ["reverse"])
    assert arr == [4, 3, 2, 1]