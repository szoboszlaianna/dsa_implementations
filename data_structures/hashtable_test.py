from hashtable import HashTable
import pytest


def test_should_create_hashtable():
    """
    Test case to verify if a HashTable object can be created with a specified size.
    """
    assert HashTable(size=100) is not None


def test_should_report_size():
    """
    Test case to verify if the size of the HashTable object can be retrieved.
    """
    assert len(HashTable(size=100)) == 100


def test_should_create_empty_value_in_hashtable():
    """
    Test case to verify if an empty HashTable object can be created with a specified size.
    """
    expected = [None, None, None]
    assert HashTable(size=3).data == expected


def test_should_insert_key_value_pairs():
    """
    Test case to verify if a key-value pair can be inserted into the HashTable object.
    """
    hash_table = HashTable(size=100)

    hash_table["hello"] = "world"
    hash_table[3.14] = "pi"
    assert hash_table["hello"] == "world"
    assert hash_table[3.14] == "pi"


def test_should_raise_key_error_on_empty_hashtable():
    """
    Test case to verify if a KeyError is raised when trying to retrieve a key from an empty HashTable object.
    """
    hash_table = HashTable(size=100)
    with pytest.raises(KeyError):
        hash_table["hello"]


def test_should_raise_key_error_on_missing_key():
    """
    Test case to verify if a KeyError is raised when trying to retrieve a missing key from a HashTable object.
    """
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    with pytest.raises(KeyError):
        hash_table["pi"]


def test_should_get_value_by_key():
    """
    Test case to verify if the value associated with a key can be retrieved from a HashTable object.
    """
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    assert hash_table["hello"] == "world"


def test_remove_key_value_pair():
    """
    Test case to verify if a key-value pair can be removed from a HashTable object.
    """
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    assert hash_table["hello"] == "world"
    del hash_table["hello"]


def test_remove_key_error():
    """
    Test case to verify if a KeyError is raised when trying to remove a missing key from a HashTable object.
    """
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    with pytest.raises(KeyError):
        del hash_table["pi"]


def test_remove_on_empty_hashtable():
    """
    Test case to verify if a KeyError is raised when trying to remove a key from an empty HashTable object.
    """
    hash_table = HashTable(size=100)
    with pytest.raises(KeyError):
        del hash_table["hello"]


def test_get_missing_key_with_default():
    """
    Test case to verify if the default value is returned when trying to retrieve a missing key from a HashTable object.
    """
    hash_table = HashTable(size=100)
    value = hash_table.get("not_found", "default_value")
    assert value == "default_value"


def test_get_existing_key():
    """
    Test case to verify if the value associated with a key can be retrieved from a HashTable object.
    """
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    value = hash_table.get("hello")
    assert value == "world"


def test_should_handle_collisions():
    """
    Test case to verify if the HashTable handles collisions correctly.
    """
    hash_table = HashTable(size=2)

    hash_table["hello"] = "world"
    hash_table["friend"] = "good"

    assert hash_table["hello"] == "world"
    assert hash_table["friend"] == "good"