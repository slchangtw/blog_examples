import pytest

from remove_duplicates import remove_duplicates

@pytest.mark.parametrize(
    "input, expected",
    [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 1], [1, 2, 3]),
        ([1, 1, 1, 1], [1]),
    ],
)
def test_remove_duplicates(input, expected):
    assert remove_duplicates(input) == expected
