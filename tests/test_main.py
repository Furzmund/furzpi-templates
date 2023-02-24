from __future__ import annotations
from unittest import mock

import pytest
from faker import Faker

from src.tools.msg import in_range
from src.tools.msg import get_time_of_day
from src.tools.msg import message


generator = Faker()


@pytest.mark.parametrize(
    "msg",
    [
        (" "),
        (generator.word()),
        (generator.word()),
    ],
)
def test_message(msg, capsys):
        message(msg)
        captured = capsys.readouterr()
        assert captured.out == msg + "\n"


@pytest.mark.parametrize(
    "min,max,val,expected",
    [
        (0, 10, 5, True),
        (0, 10, 12, False),
        (-10, 20, 14, True),
        (-10, 20, -15, False),
        (-10000, 10000, 3742, True),
        (-10000, 10000, 93742, False),
    ],
)
def test_in_range(min, max, val, expected):
    result = in_range(min, max, val)
    assert result == expected


@pytest.mark.parametrize(
    "min,max,val",
    [
        (10, 5, 0),
        (123, -234, 0),
        (10, 9, 0),
    ]
)
def test_in_range_bad_input(min, max, val):
    with pytest.raises(AssertionError):
        result = in_range(min, max, val)


@pytest.mark.parametrize(
    "hour,expected",
    [
        (0, "Morgen"),
        (3, "Morgen"),
        (11, "Morgen"),
        (12, "Tag"),
        (15, "Tag"),
        (16, "Tag"),
        (17, "Abend"),
        (19, "Abend"),
        (21, "Abend"),
        (22, "Nacht"),
        (23, "Nacht"),
        (24, "Nacht"),
    ],
)
def test_get_time_of_day(hour, expected):
    tod = get_time_of_day(hour)
    assert tod == expected
