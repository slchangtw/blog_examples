import pytest

from duplicate_remover import DuplicateRemover


@pytest.fixture(name="duplicate_remover")
def fixture_duplicate_remover():
    return DuplicateRemover()


@pytest.mark.parametrize(
    "input, expected",
    [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([2, 1, 3, 1], [2, 1, 3]),
        ([1, 1, 1, 1], [1]),
    ],
)
def test_remove_duplicates_from_list(input, expected, duplicate_remover):
    assert duplicate_remover.remove_duplicates_from_list(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ((), ()),
        ((1, 2, 3), (1, 2, 3)),
        ((2, 1, 3, 1), (2, 1, 3)),
        ((1, 1, 1, 1), tuple([1])),
    ],
)
def test_remove_duplicates_from_tuple(input, expected, duplicate_remover):
    assert duplicate_remover.remove_duplicates_from_tuple(input) == expected
