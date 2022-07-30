import pytest


def filter_list(l):
    filt = [l[i] for i in range(len(l)) if type(l[i]) is int]
    return filt


def test_solution():
    assert filter_list([1, 2, "a", "b"]) == [1, 2]
    assert filter_list([1, "a", "b", 0, 15]) == [1, 0, 15]
