__author__ = 'Aleksander Chrabaszcz'


def is_integral(n):
    return int(n) == n

LOCALES = {
    "en": {
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: "p" if not is_integral(n) else ("" if n == 1 else "h"),
        "format": {
            "decimal_point": ".",
            "date": "%-d/%-m/%Y",
            "date_short": "%-d/%-m",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p",
            "datetime": "%-I:%M:%S %p %-d/%-m/%Y",
            "datetime_short": "%-I:%M %p %-d/%-m",
        },
    },
    "en-US": {
        "name": "US English",
        "native_name": "US English",
        "number_rule": lambda n: "p" if not is_integral(n) else ("" if n == 1 else "h"),
        "format": {
            "decimal_point": ".",
            "date": "%-m/%-d/%Y",  # http://strftime.org/
            "date_short": "%-m/%-d",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p",
            "datetime": "%-I:%M:%S %p %-m/%-d/%Y",
            "datetime_short": "%-I:%M %p %-m/%-d",
        },
    },
    "en-GB": {
        "name": "British English",
        "native_name": "British English",
        "number_rule": lambda n: "p" if not is_integral(n) else ("" if n == 1 else "h"),
        "format": {
            "decimal_point": ".",
            "date": "%-d/%-m/%Y",
            "date_short": "%-d/%-m",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p",
            "datetime": "%-I:%M:%S %p %-d/%-m/%Y",
            "datetime_short": "%-I:%M %p %-d/%-m",
        },
    },
    "pl": {
        "name": "Polish",
        "native_name": "Polski",
        "number_rule": lambda n: "p" if not is_integral(n) else ("" if n == 1 else
            ("f" if n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14] else "h")),
        "format": {
            "decimal_point": ",",
            "date": "%-d.%-m.%Y",
            "date_short": "%-d.%-m",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M",
            "datetime": "%-H:%M:%S %-d.%-m.%Y",
            "datetime_short": "%-H:%M %-d.%-m",
        },
    }
}

