from hashtable import HashTable
import pytest


def test_should_create_hashtable():
    assert HashTable(size=100) is not None


def test_should_report_size():
    assert len(HashTable(size=100)) == 100


def test_should_create_empty_value_in_hashtable():
    expected = [None, None, None]
    assert HashTable(size=3).data == expected


def test_should_insert_key_value_pairs():
    hash_table = HashTable(size=100)

    hash_table["hello"] = "world"
    hash_table[3.14] = "pi"
    assert hash_table["hello"] == "world"
    assert hash_table[3.14] == "pi"


def test_should_raise_key_error_on_empty_hashtable():
    hash_table = HashTable(size=100)
    with pytest.raises(KeyError):
        hash_table["hello"]


def test_should_raise_key_error_on_missing_key():
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    with pytest.raises(KeyError):
        hash_table["pi"]


def test_should_get_value_by_key():
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    assert hash_table["hello"] == "world"


def test_remove_key_value_pair():
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    assert hash_table["hello"] == "world"
    del hash_table["hello"]


def test_remove_key_error():
    hash_table = HashTable(size=100)
    hash_table["hello"] = "world"
    with pytest.raises(KeyError):
        del hash_table["pi"]


def test_remove_on_empty_hashtable():
    hash_table = HashTable(size=100)
    with pytest.raises(KeyError):
        del hash_table["hello"]