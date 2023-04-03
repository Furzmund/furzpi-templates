from __future__ import annotations

import sys
from datetime import datetime

from .tools.msg import get_time_of_day
from .tools.msg import message


def main():
    try:
        hour = datetime.now().hour
        tod = get_time_of_day(hour)
        if tod.lower() == "nacht":
            prefix = "Gute"
        else:
            prefix = "Guten"
        message(f"{prefix} {tod}")
    except Exception:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
