__author__ = 'Aleksander Chrabaszcz'


def is_integral(n):
    return int(n) == n

LOCALES = {
    "en": {
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: "m" if not is_integral(n) else ("" if n == 1 else "m"),
        "format": {
            "decimal_point": ".",
            "date": "%-m/%-d/%Y",  # http://strftime.org/
            "time": "%-I:%M:%S %p",
            "datetime": "%-I:%M:%S %p %-m/%-d/%Y",
        },
    },
    "en_GB": {
        "name": "British English",
        "native_name": "British English",
        "number_rule": lambda n: "m" if not is_integral(n) else ("" if n == 1 else "m"),
        "format": {
            "decimal_point": ".",
            "date": "%-d/%-m/%Y",
            "time": "%-I:%M:%S %p",
            "datetime": "%-I:%M:%S %p %-d/%-m/%Y",
        },
    },
    "pl": {
        "name": "Polish",
        "native_name": "Polski",
        "number_rule": lambda n: "o" if not is_integral(n) else ("" if n == 1 else
            ("f" if n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14] else "m")),
        "format": {
            "decimal_point": ",",
            "date": "%-d.%-m.%Y",
            "time": "%-H:%M:%S",
            "datetime": "%-H:%M:%S %-d.%-m.%Y",
        },
    }
}
