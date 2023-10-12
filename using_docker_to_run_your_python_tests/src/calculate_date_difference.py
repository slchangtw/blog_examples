import pendulum


def calculate_date_difference(
    start_date: pendulum.Date, end_date: pendulum.Date
) -> int:
    difference = end_date - start_date
    return difference.days
