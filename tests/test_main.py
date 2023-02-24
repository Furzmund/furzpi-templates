from __future__ import annotations

import pytest
from faker import Faker

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
def test_message(msg):
    message(msg)


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
