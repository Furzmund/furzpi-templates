from __future__ import annotations

import sys


def message(input: str) -> None:
    """
    Send a message to the standard output
    :param input: string
    """
    sys.stdout.write(f"{input}\n")


def in_range(min: int, max: int, val: int) -> bool:
    """
    Check if value is in the minimum and maximum of the range
    :param min: minimum value
    :param max: maximum value
    :param value: value to test
    :returns boolean
    """
    assert min <= max, "Min must be less than or equal to max"
    return min <= val <= max


def get_time_of_day(hour: int) -> str:
    """
    Use the machine's time to determine the time of day
    :param hour: 24-hour integer value (0-24)
    :returns a string with the time of day, i.e. Morning
    """
    TIMES_OF_DAY = [
        [(0, 11), "Morgen"],
        [(12, 16), "Tag"],
        [(17, 21), "Abend"],
        [(22, 24), "Nacht"],
    ]
    time_of_day: str = ""
    for tod in TIMES_OF_DAY:
        min, max = tod[0]
        if in_range(min, max, hour):  # type: ignore
            time_of_day = tod[1]  # type: ignore
            break
    return time_of_day
