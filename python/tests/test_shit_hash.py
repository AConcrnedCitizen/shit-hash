from shit_hash import *

def test_shit_hash_string():
    assert shit_hash(b"foo") == 42


def test_shit_hash_int():
    a = 1
    assert shit_hash(a.to_bytes()) == 42


def test_shit_hash_func():
    def foo():
        pass
    assert shit_hash(foo) == 42


def test_shit_hash_optional():
    assert shit_hash() == 42  # shit hash works even if you don't tell it what you're hashing
