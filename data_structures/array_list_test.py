from array_list import ArrayList
import pytest


def test_should_create_array_list():
    """
    Test case to verify if a ArrayList object can be created with a specified size.
    """
    assert ArrayList(capacity=10) is not None


def test_str():
    """
    Test case to verify if the string representation of an ArrayList object can be retrieved.
    """
    assert str(ArrayList(capacity=10)) == "[]"


def test_should_create_empty_array_list():
    """
    Test case to verify if an empty ArrayList object can be created with a specified size.
    """
    expected = [None, None, None, None, None, None, None, None, None, None]
    assert ArrayList(capacity=10).data == expected


def test_getitem():
    """
    Test case to verify if the value at an index can be retrieved from an ArrayList object.
    """
    array_list = ArrayList(capacity=10)
    array_list.data[0] = 1
    assert array_list.data[0] == 1


def test_getitem_out_of_bounds():
    """
    Test case to verify if an IndexError is raised when trying to retrieve an index out of bounds from an ArrayList object.
    """
    array_list = ArrayList(capacity=10)
    with pytest.raises(IndexError):
        array_list.data[10]


def test_setitem():
    """
    Test case to verify if the value at an index can be set in an ArrayList object.
    """
    array_list = ArrayList(capacity=10)
    array_list.data[0] = 1
    assert array_list.data[0] == 1


def test_setitem_out_of_bounds():
    """
    Test case to verify if an IndexError is raised when trying to set an index out of bounds in an ArrayList object.
    """
    array_list = ArrayList(capacity=10)
    with pytest.raises(IndexError):
        array_list.data[10] = 1


def test_resize():
    """
    Test case to verify if the internal capacity of the ArrayList object can be increased when resizing.
    """
    array_list = ArrayList(capacity=3)
    array_list._resize(4)
    assert len(array_list.data) == 4


def test_add():
    """
    Test case to verify if a value can be added to an ArrayList object.
    """
    array_list = ArrayList(capacity=10)
    array_list.add(1)
    assert array_list.data[0] == 1


def test_add_trigger_resize():
    """
    Test case to verify if the size of the ArrayList object can be increased when adding a value.
    """
    array_list = ArrayList(capacity=3)
    array_list.add(1)
    array_list.add(2)
    array_list.add(3)
    array_list.add(4)
    assert len(array_list) == 4


def test_remove():
    """
    Test case to verify if a value can be removed from an ArrayList object.
    """
    array_list = ArrayList(capacity=10)
    array_list.add(1)
    array_list.add(2)
    array_list.add(3)
    array_list.add(4)
    array_list.remove(2)
    print(array_list.data)
    assert array_list.data[0] is 1
    assert array_list.data[1] is 2
    assert array_list.data[2] is 4
    assert array_list.size == 3


def test_remove_out_of_bounds():
    """
    Test case to verify if an IndexError is raised when trying to remove an index out of bounds from an ArrayList object.
    """
    array_list = ArrayList(capacity=10)
    with pytest.raises(IndexError):
        array_list.remove(10)


def test_remove_trigger_resize():
    """
    Test case to verify if the internal capacity of the ArrayList object can be decreased when removing values.
    """
    array_list = ArrayList(capacity=3)

    for i in range(30):
        array_list.add(i)

    assert len(array_list.data) > 3

    initial_capacity = len(array_list.data)

    for _ in range(25):
        array_list.remove(0)

    final_capacity = len(array_list.data)

    assert final_capacity < initial_capacity
    assert array_list.size == 5
    assert array_list.data[:5] == [25, 26, 27, 28, 29]
