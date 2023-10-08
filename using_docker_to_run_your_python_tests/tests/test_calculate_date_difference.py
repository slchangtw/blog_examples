import pendulum
import pytest

from src.calculate_date_difference import calculate_date_difference


@pytest.mark.parametrize(
    "date_1, date_2, expected",
    [
        ((2023, 1, 1), (2023, 1, 10), 9),
        ((2023, 1, 1), (2023, 1, 1), 0),
        ((2023, 1, 10), (2023, 1, 1), -9),
    ],
)
def test_calculate_date_difference(date_1, date_2, expected):
    start_date = pendulum.datetime(*date_1)
    end_date = pendulum.datetime(*date_2)
    assert calculate_date_difference(start_date, end_date) == expected
