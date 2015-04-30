def is_integral(n):
    return int(n) == n

LOCALES = {
    "af": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %-I:%M:%S %p",
            "datetime_short": "%Y-%m-%-d %-I:%M %p",
            "decimal_point": ",",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Afrikaans",
        "native_name": "Afrikaans",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "af-NA": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %-I:%M:%S %p",
            "datetime_short": "%Y-%m-%-d %-I:%M %p",
            "decimal_point": ",",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Afrikaans",
        "native_name": "Afrikaans",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "af-ZA": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %-I:%M:%S %p",
            "datetime_short": "%Y-%m-%-d %-I:%M %p",
            "decimal_point": ",",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Afrikaans",
        "native_name": "Afrikaans",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "am": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Amharic",
        "native_name": "\u12a0\u121b\u122d\u129b",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ar": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-001": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-AE": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-BH": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-DJ": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-DZ": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-EH": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-ER": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-IL": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-IQ": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-JO": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-KM": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-KW": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-LB": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-LY": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-MA": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-MR": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-OM": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-PS": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-QA": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-SA": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-SD": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-SO": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-SS": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-SY": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-TD": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-TN": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "ar-YE": {
        "format": {
            "date": "%-d\u200f/%m\u200f/%Y",
            "datetime": "%-d\u200f/%m\u200f/%Y %-I:%M:%S %p",
            "datetime_short": "%-d\u200f/%m\u200f/%Y %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Arabic",
        "native_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('z' if n == 0 else '' if n == 1 else 't' if n == 2 else 'w' if n % 100 >= 3 and n % 100 <= 10 else 'y' if n % 100 >= 11 else 'p')
    },
    "az": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Azeri",
        "native_name": "az\u0259rbaycan",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "az-Cyrl_AZ": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Azeri",
        "native_name": "az\u0259rbaycan",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "az-Latn": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Azeri",
        "native_name": "az\u0259rbaycan",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "az-Latn_AZ": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Azeri",
        "native_name": "az\u0259rbaycan",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "bg": {
        "format": {
            "date": "%-d.%m.%Y '\u0433'.",
            "datetime": "%-d.%m.%Y '\u0433'., %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y '\u0433'., %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Bulgarian",
        "native_name": "\u0431\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "bn": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Bengali",
        "native_name": "\u09ac\u09be\u0982\u09b2\u09be",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "bn-BD": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Bengali",
        "native_name": "\u09ac\u09be\u0982\u09b2\u09be",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "bn-IN": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Bengali",
        "native_name": "\u09ac\u09be\u0982\u09b2\u09be",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "bs": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y. %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Bosnian",
        "native_name": "bosanski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "bs-Cyrl_BA": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y. %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Bosnian",
        "native_name": "bosanski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "bs-Latn": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y. %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Bosnian",
        "native_name": "bosanski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "bs-Latn_BA": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y. %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Bosnian",
        "native_name": "bosanski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "ca": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Catalan",
        "native_name": "catal\u00e0",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ca-AD": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Catalan",
        "native_name": "catal\u00e0",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ca-ES": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Catalan",
        "native_name": "catal\u00e0",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ca-FR": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Catalan",
        "native_name": "catal\u00e0",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ca-IT": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Catalan",
        "native_name": "catal\u00e0",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "cs": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Czech",
        "native_name": "\u010de\u0161tina",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if (n == 1) else 'w' if (n >= 2 and n <= 4) else 'p')
    },
    "cy": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Welsh",
        "native_name": "Cymraeg",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if (n == 1) else 't' if (n == 2) else 'p' if (n != 8 and n != 11) else 'y')
    },
    "da": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H.%M.%S",
            "datetime_short": "%-d/%m/%Y %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Danish",
        "native_name": "dansk",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "da-DK": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H.%M.%S",
            "datetime_short": "%-d/%m/%Y %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Danish",
        "native_name": "dansk",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "da-GL": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H.%M.%S",
            "datetime_short": "%-d/%m/%Y %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Danish",
        "native_name": "dansk",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "de": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "German",
        "native_name": "Deutsch",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "de-AT": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "German",
        "native_name": "Deutsch",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "de-BE": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "German",
        "native_name": "Deutsch",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "de-DE": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "German",
        "native_name": "Deutsch",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "de-LI": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "German",
        "native_name": "Deutsch",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "de-LU": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "German",
        "native_name": "Deutsch",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "dz": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d \u0f46\u0f74\u0f0b\u0f5a\u0f7c\u0f51\u0f0b%-I:%M:%S %p",
            "datetime_short": "%Y-%m-%-d \u0f46\u0f74\u0f0b\u0f5a\u0f7c\u0f51\u0f0b %-I \u0f66\u0f90\u0f62\u0f0b\u0f58\u0f0b %M %p",
            "decimal_point": ".",
            "time": "\u0f46\u0f74\u0f0b\u0f5a\u0f7c\u0f51\u0f0b%-I:%M:%S %p",
            "time_short": "\u0f46\u0f74\u0f0b\u0f5a\u0f7c\u0f51\u0f0b %-I \u0f66\u0f90\u0f62\u0f0b\u0f58\u0f0b %M %p"
        },
        "name": "Dzongkha",
        "native_name": "\u0f62\u0fab\u0f7c\u0f44\u0f0b\u0f41",
        "number_rule": lambda n: ''
    },
    "el": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": ",",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Greek",
        "native_name": "\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "el-CY": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": ",",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Greek",
        "native_name": "\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "el-GR": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": ",",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Greek",
        "native_name": "\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en": {
        "format": {
            "date": "%-d/%-m/%Y",
            "datetime": "%-d/%-m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%-m/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-001": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-150": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-AG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-AI": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-AS": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-BB": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-BE": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-BM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-BS": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-BW": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-BZ": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-CA": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-CC": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-CK": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-CM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-CX": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-DG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-DM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-ER": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-FJ": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-FK": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-FM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-GB": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-GD": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-GG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-GH": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-GI": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-GM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-GU": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-GY": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-HK": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-IE": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-IM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-IN": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-IO": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-JE": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-JM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-KE": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-KI": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-KN": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-KY": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-LC": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-LR": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-LS": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MH": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MO": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MP": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MS": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MT": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MU": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MW": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-MY": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-NA": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-NF": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-NG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-NR": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-NU": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-NZ": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-PG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-PH": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-PK": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-PN": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-PR": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-PW": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-RW": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SB": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SC": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SD": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SH": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SL": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SS": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SX": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-SZ": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-TC": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-TK": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-TO": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-TT": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-TV": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-TZ": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-UG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-UM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-US": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-VC": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-VG": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-VI": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-VU": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-WS": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-ZA": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-ZM": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "en-ZW": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y, %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "English",
        "native_name": "English",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-AR": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-BO": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-CO": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-CR": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-CU": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-DO": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-EA": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-EC": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-ES": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-GQ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-GT": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-HN": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-IC": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-NI": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-PA": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-PE": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-PH": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-PR": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-PY": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-SV": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-US": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-UY": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "es-VE": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Spanish",
        "native_name": "espa\u00f1ol",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "et": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M.%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M.%S",
            "time_short": "%-H:%M"
        },
        "name": "Estonian",
        "native_name": "eesti",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "eu": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Basque",
        "native_name": "euskara",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fa": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d\u060c\u200f %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d\u060c\u200f %-H:%M",
            "decimal_point": "\u066b",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Persian",
        "native_name": "\u0641\u0627\u0631\u0633\u06cc",
        "number_rule": lambda n: ''
    },
    "fi": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Finnish",
        "native_name": "suomi",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fo": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Faroese",
        "native_name": "f\u00f8royskt",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-BE": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-BF": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-BI": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-BJ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-BL": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-CD": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-CF": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-CG": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-CH": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-CI": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-CM": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-DJ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-DZ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-FR": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-GA": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-GF": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-GN": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-GP": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-GQ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-HT": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-KM": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-LU": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-MA": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-MC": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-MF": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-MG": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-ML": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-MQ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-MR": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-MU": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-NC": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-NE": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-PF": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-PM": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-RE": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-RW": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-SC": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-SN": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-SY": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-TD": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-TG": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-TN": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-VU": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-WF": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fr-YT": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "French",
        "native_name": "fran\u00e7ais",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "fy": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Western Frisian",
        "native_name": "West-Frysk",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ga": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Irish",
        "native_name": "Gaeilge",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 't' if n == 2 else 't' if (n > 2 and n < 7) else 'y' if (n > 6 and n < 11) else 'p')
    },
    "gd": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Scottish Gaelic",
        "native_name": "G\u00e0idhlig",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if (n == 1 or n == 11) else 't' if (n == 2 or n == 12) else 'w' if (n > 2 and n < 20) else 'p')
    },
    "gl": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Galician",
        "native_name": "galego",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "gu": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Gujarati",
        "native_name": "\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "he": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Hebrew",
        "native_name": "\u05e2\u05d1\u05e8\u05d9\u05ea",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "hi": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Hindi",
        "native_name": "\u0939\u093f\u0928\u094d\u0926\u0940",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "hr": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y. %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Croatian",
        "native_name": "hrvatski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "hr-BA": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y. %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Croatian",
        "native_name": "hrvatski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "hr-HR": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y. %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Croatian",
        "native_name": "hrvatski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "hu": {
        "format": {
            "date": "%Y. %m. %-d.",
            "datetime": "%Y. %m. %-d. %-H:%M:%S",
            "datetime_short": "%Y. %m. %-d. %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Hungarian",
        "native_name": "magyar",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "hy": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Armenian",
        "native_name": "\u0570\u0561\u0575\u0565\u0580\u0565\u0576",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "id": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H.%M.%S",
            "datetime_short": "%-d/%m/%Y %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Indonesian",
        "native_name": "Bahasa Indonesia",
        "number_rule": lambda n: ''
    },
    "is": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Icelandic",
        "native_name": "\u00edslenska",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('p' if (n % 10 != 1 or n % 100 == 11) else '')
    },
    "it": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Italian",
        "native_name": "italiano",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "it-CH": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Italian",
        "native_name": "italiano",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "it-IT": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Italian",
        "native_name": "italiano",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "it-SM": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Italian",
        "native_name": "italiano",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ja": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Japanese",
        "native_name": "\u65e5\u672c\u8a9e",
        "number_rule": lambda n: ''
    },
    "ka": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Georgian",
        "native_name": "\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8",
        "number_rule": lambda n: ''
    },
    "kk": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Kazakh",
        "native_name": "\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456",
        "number_rule": lambda n: ''
    },
    "kk-Cyrl": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Kazakh",
        "native_name": "\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456",
        "number_rule": lambda n: ''
    },
    "kk-Cyrl_KZ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Kazakh",
        "native_name": "\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456",
        "number_rule": lambda n: ''
    },
    "kl": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %-I:%M:%S %p",
            "datetime_short": "%Y-%m-%-d %-I:%M %p",
            "decimal_point": ",",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Kalaallisut",
        "native_name": "kalaallisut",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "km": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": ",",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Khmer",
        "native_name": "\u1781\u17d2\u1798\u17c2\u179a",
        "number_rule": lambda n: ''
    },
    "kn": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Kannada",
        "native_name": "\u0c95\u0ca8\u0ccd\u0ca8\u0ca1",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ko": {
        "format": {
            "date": "%Y. %m. %-d.",
            "datetime": "%Y. %m. %-d. %p %-I:%M:%S",
            "datetime_short": "%Y. %m. %-d. %p %-I:%M",
            "decimal_point": ".",
            "time": "%p %-I:%M:%S",
            "time_short": "%p %-I:%M"
        },
        "name": "Korean",
        "native_name": "\ud55c\uad6d\uc5b4",
        "number_rule": lambda n: ''
    },
    "ko-KP": {
        "format": {
            "date": "%Y. %m. %-d.",
            "datetime": "%Y. %m. %-d. %p %-I:%M:%S",
            "datetime_short": "%Y. %m. %-d. %p %-I:%M",
            "decimal_point": ".",
            "time": "%p %-I:%M:%S",
            "time_short": "%p %-I:%M"
        },
        "name": "Korean",
        "native_name": "\ud55c\uad6d\uc5b4",
        "number_rule": lambda n: ''
    },
    "ko-KR": {
        "format": {
            "date": "%Y. %m. %-d.",
            "datetime": "%Y. %m. %-d. %p %-I:%M:%S",
            "datetime_short": "%Y. %m. %-d. %p %-I:%M",
            "decimal_point": ".",
            "time": "%p %-I:%M:%S",
            "time_short": "%p %-I:%M"
        },
        "name": "Korean",
        "native_name": "\ud55c\uad6d\uc5b4",
        "number_rule": lambda n: ''
    },
    "ks": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Kashmiri",
        "native_name": "\u06a9\u0672\u0634\u064f\u0631",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ks-Arab": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Kashmiri",
        "native_name": "\u06a9\u0672\u0634\u064f\u0631",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ks-Arab_IN": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Kashmiri",
        "native_name": "\u06a9\u0672\u0634\u064f\u0631",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ky": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Kirghiz",
        "native_name": "\u043a\u044b\u0440\u0433\u044b\u0437\u0447\u0430",
        "number_rule": lambda n: ''
    },
    "ky-Cyrl": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Kirghiz",
        "native_name": "\u043a\u044b\u0440\u0433\u044b\u0437\u0447\u0430",
        "number_rule": lambda n: ''
    },
    "ky-Cyrl_KG": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Kirghiz",
        "native_name": "\u043a\u044b\u0440\u0433\u044b\u0437\u0447\u0430",
        "number_rule": lambda n: ''
    },
    "lb": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Luxembourgish",
        "native_name": "L\u00ebtzebuergesch",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "lo": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Lao",
        "native_name": "\u0ea5\u0eb2\u0ea7",
        "number_rule": lambda n: ''
    },
    "lt": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Lithuanian",
        "native_name": "lietuvi\u0173",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "lv": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Latvian",
        "native_name": "latvie\u0161u",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'p' if n != 0 else 'z')
    },
    "mk": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Macedonian",
        "native_name": "\u043c\u0430\u043a\u0435\u0434\u043e\u043d\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ml": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Malayalam",
        "native_name": "\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "mn": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d, %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d, %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Mongolian",
        "native_name": "\u043c\u043e\u043d\u0433\u043e\u043b",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "mn-Cyrl": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d, %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d, %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Mongolian",
        "native_name": "\u043c\u043e\u043d\u0433\u043e\u043b",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "mn-Cyrl_MN": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d, %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d, %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Mongolian",
        "native_name": "\u043c\u043e\u043d\u0433\u043e\u043b",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "mr": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Marathi",
        "native_name": "\u092e\u0930\u093e\u0920\u0940",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ms": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Malay",
        "native_name": "Bahasa Melayu",
        "number_rule": lambda n: ''
    },
    "ms-Latn": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Malay",
        "native_name": "Bahasa Melayu",
        "number_rule": lambda n: ''
    },
    "ms-Latn_BN": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Malay",
        "native_name": "Bahasa Melayu",
        "number_rule": lambda n: ''
    },
    "ms-Latn_MY": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Malay",
        "native_name": "Bahasa Melayu",
        "number_rule": lambda n: ''
    },
    "ms-Latn_SG": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Malay",
        "native_name": "Bahasa Melayu",
        "number_rule": lambda n: ''
    },
    "my": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Burmese",
        "native_name": "\u1017\u1019\u102c",
        "number_rule": lambda n: ''
    },
    "nb": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y, %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Norwegian Bokm\u00e5l",
        "native_name": "norsk bokm\u00e5l",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nb-NO": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y, %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Norwegian Bokm\u00e5l",
        "native_name": "norsk bokm\u00e5l",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nb-SJ": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y, %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Norwegian Bokm\u00e5l",
        "native_name": "norsk bokm\u00e5l",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ne": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d, %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d, %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Nepali",
        "native_name": "\u0928\u0947\u092a\u093e\u0932\u0940",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ne-IN": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d, %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d, %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Nepali",
        "native_name": "\u0928\u0947\u092a\u093e\u0932\u0940",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ne-NP": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d, %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d, %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Nepali",
        "native_name": "\u0928\u0947\u092a\u093e\u0932\u0940",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nl": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Dutch",
        "native_name": "Nederlands",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nl-AW": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Dutch",
        "native_name": "Nederlands",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nl-BE": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Dutch",
        "native_name": "Nederlands",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nl-BQ": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Dutch",
        "native_name": "Nederlands",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nl-CW": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Dutch",
        "native_name": "Nederlands",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nl-NL": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Dutch",
        "native_name": "Nederlands",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nl-SR": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Dutch",
        "native_name": "Nederlands",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nl-SX": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-H:%M:%S",
            "datetime_short": "%-d-%m-%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Dutch",
        "native_name": "Nederlands",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "nn": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Norwegian Nynorsk",
        "native_name": "nynorsk",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "os": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Ossetic",
        "native_name": "\u0438\u0440\u043e\u043d",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "os-GE": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Ossetic",
        "native_name": "\u0438\u0440\u043e\u043d",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "os-RU": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Ossetic",
        "native_name": "\u0438\u0440\u043e\u043d",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pa": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Punjabi",
        "native_name": "\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pa-Arab_PK": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Punjabi",
        "native_name": "\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pa-Guru": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Punjabi",
        "native_name": "\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pa-Guru_IN": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y, %-I:%M %p",
            "decimal_point": "\u066b",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Punjabi",
        "native_name": "\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pl": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Polish",
        "native_name": "polski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "pt": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pt-AO": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pt-BR": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pt-CV": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pt-GW": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pt-MO": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pt-MZ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pt-ST": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "pt-TL": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Portuguese",
        "native_name": "portugu\u00eas",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ro": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Romanian",
        "native_name": "rom\u00e2n\u0103",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'w' if (n == 0 or (n % 100 > 0 and n % 100 < 20)) else 'p')
    },
    "ro-MD": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Romanian",
        "native_name": "rom\u00e2n\u0103",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'w' if (n == 0 or (n % 100 > 0 and n % 100 < 20)) else 'p')
    },
    "ro-RO": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Romanian",
        "native_name": "rom\u00e2n\u0103",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'w' if (n == 0 or (n % 100 > 0 and n % 100 < 20)) else 'p')
    },
    "ru": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Russian",
        "native_name": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "ru-BY": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Russian",
        "native_name": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "ru-KG": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Russian",
        "native_name": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "ru-KZ": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Russian",
        "native_name": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "ru-MD": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Russian",
        "native_name": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "ru-RU": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Russian",
        "native_name": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "ru-UA": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Russian",
        "native_name": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "si": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %p %-I.%M.%S",
            "datetime_short": "%Y-%m-%-d %p %-I.%M",
            "decimal_point": ".",
            "time": "%p %-I.%M.%S",
            "time_short": "%p %-I.%M"
        },
        "name": "Sinhala",
        "native_name": "\u0dc3\u0dd2\u0d82\u0dc4\u0dbd",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sk": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Slovak",
        "native_name": "sloven\u010dina",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if (n == 1) else 'w' if (n >= 2 and n <= 4) else 'p')
    },
    "sl": {
        "format": {
            "date": "%-d. %m. %Y",
            "datetime": "%-d. %m. %Y %-H:%M:%S",
            "datetime_short": "%-d. %m. %Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Slovenian",
        "native_name": "sloven\u0161\u010dina",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 100 == 1 else 't' if n % 100 == 2 else 'w' if n % 100 == 3 or n % 100 == 4 else 'p')
    },
    "sq": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Albanian",
        "native_name": "shqip",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sq-AL": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Albanian",
        "native_name": "shqip",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sq-MK": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Albanian",
        "native_name": "shqip",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sq-XK": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y, %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y, %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Albanian",
        "native_name": "shqip",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sr": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Cyrl": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Cyrl_BA": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Cyrl_ME": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Cyrl_RS": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Cyrl_XK": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Latn": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "srpski",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Latn_BA": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Latn_ME": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Latn_RS": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sr-Latn_XK": {
        "format": {
            "date": "%-d.%m.%Y.",
            "datetime": "%-d.%m.%Y. %-H.%M.%S",
            "datetime_short": "%-d.%m.%Y. %-H.%M",
            "decimal_point": ",",
            "time": "%-H.%M.%S",
            "time_short": "%-H.%M"
        },
        "name": "Serbian",
        "native_name": "\u0441\u0440\u043f\u0441\u043a\u0438",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "sv": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Swedish",
        "native_name": "svenska",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sv-AX": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Swedish",
        "native_name": "svenska",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sv-SE": {
        "format": {
            "date": "%Y-%m-%-d",
            "datetime": "%Y-%m-%-d %-H:%M:%S",
            "datetime_short": "%Y-%m-%-d %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Swedish",
        "native_name": "svenska",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sw": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Swahili",
        "native_name": "Kiswahili",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sw-KE": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Swahili",
        "native_name": "Kiswahili",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sw-TZ": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Swahili",
        "native_name": "Kiswahili",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "sw-UG": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Swahili",
        "native_name": "Kiswahili",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ta": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y, %-I:%M:%S %p",
            "datetime_short": "%-d-%m-%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Tamil",
        "native_name": "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ta-IN": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y, %-I:%M:%S %p",
            "datetime_short": "%-d-%m-%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Tamil",
        "native_name": "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ta-LK": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y, %-I:%M:%S %p",
            "datetime_short": "%-d-%m-%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Tamil",
        "native_name": "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ta-MY": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y, %-I:%M:%S %p",
            "datetime_short": "%-d-%m-%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Tamil",
        "native_name": "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ta-SG": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y, %-I:%M:%S %p",
            "datetime_short": "%-d-%m-%Y, %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Tamil",
        "native_name": "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "te": {
        "format": {
            "date": "%-d-%m-%Y",
            "datetime": "%-d-%m-%Y %-I:%M:%S %p",
            "datetime_short": "%-d-%m-%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Telugu",
        "native_name": "\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "th": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Thai",
        "native_name": "\u0e44\u0e17\u0e22",
        "number_rule": lambda n: ''
    },
    "to": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Tongan",
        "native_name": "lea fakatonga",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "tr": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Turkish",
        "native_name": "T\u00fcrk\u00e7e",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "tr-CY": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Turkish",
        "native_name": "T\u00fcrk\u00e7e",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "tr-TR": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Turkish",
        "native_name": "T\u00fcrk\u00e7e",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ug": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y\u060c %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y\u060c %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Uighur",
        "native_name": "\u0626\u06c7\u064a\u063a\u06c7\u0631\u0686\u06d5",
        "number_rule": lambda n: ''
    },
    "ug-Arab": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y\u060c %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y\u060c %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Uighur",
        "native_name": "\u0626\u06c7\u064a\u063a\u06c7\u0631\u0686\u06d5",
        "number_rule": lambda n: ''
    },
    "ug-Arab_CN": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y\u060c %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y\u060c %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Uighur",
        "native_name": "\u0626\u06c7\u064a\u063a\u06c7\u0631\u0686\u06d5",
        "number_rule": lambda n: ''
    },
    "uk": {
        "format": {
            "date": "%-d.%m.%Y",
            "datetime": "%-d.%m.%Y %-H:%M:%S",
            "datetime_short": "%-d.%m.%Y %-H:%M",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Ukrainian",
        "native_name": "\u0443\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n % 10 == 1 and n % 100 != 11 else 'w' if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 'p')
    },
    "ur": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Urdu",
        "native_name": "\u0627\u0631\u062f\u0648",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "ur-PK": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y %-I:%M:%S %p",
            "datetime_short": "%-d/%m/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Urdu",
        "native_name": "\u0627\u0631\u062f\u0648",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "uz": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d %-H:%M",
            "decimal_point": "\u066b",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Uzbek",
        "native_name": "o\u02bbzbekcha",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "uz-Arab_AF": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d %-H:%M",
            "decimal_point": "\u066b",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Uzbek",
        "native_name": "o\u02bbzbekcha",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "uz-Cyrl": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d %-H:%M",
            "decimal_point": "\u066b",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Uzbek",
        "native_name": "\u040e\u0437\u0431\u0435\u043a",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "uz-Cyrl_UZ": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d %-H:%M",
            "decimal_point": "\u066b",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Uzbek",
        "native_name": "o\u02bbzbekcha",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "uz-Latn": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d %-H:%M",
            "decimal_point": "\u066b",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Uzbek",
        "native_name": "o\u02bbzbekcha",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "uz-Latn_UZ": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %-H:%M:%S",
            "datetime_short": "%Y/%m/%-d %-H:%M",
            "decimal_point": "\u066b",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Uzbek",
        "native_name": "o\u02bbzbekcha",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "vi": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-H:%M:%S %-d/%m/%Y",
            "datetime_short": "%-H:%M %-d/%m/%Y",
            "decimal_point": ",",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Vietnamese",
        "native_name": "Ti\u1ebfng Vi\u1ec7t",
        "number_rule": lambda n: ''
    },
    "yi": {
        "format": {
            "date": "%-d/%m/%Y",
            "datetime": "%-d/%m/%Y, %-H:%M:%S",
            "datetime_short": "%-d/%m/%Y, %-H:%M",
            "decimal_point": ".",
            "time": "%-H:%M:%S",
            "time_short": "%-H:%M"
        },
        "name": "Yiddish",
        "native_name": "\u05d9\u05d9\u05b4\u05d3\u05d9\u05e9",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    },
    "zh": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zh-Hans": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zh-Hans_CN": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zh-Hans_HK": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zh-Hans_MO": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zh-Hans_SG": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zh-Hant": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zh-Hant_MO": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zh-Hant_TW": {
        "format": {
            "date": "%Y/%m/%-d",
            "datetime": "%Y/%m/%-d %p%-I:%M:%S",
            "datetime_short": "%Y/%m/%-d %p%-I:%M",
            "decimal_point": ".",
            "time": "%p%-I:%M:%S",
            "time_short": "%p%-I:%M"
        },
        "name": "Chinese",
        "native_name": "\u4e2d\u6587",
        "number_rule": lambda n: ''
    },
    "zu": {
        "format": {
            "date": "%-m/%-d/%Y",
            "datetime": "%-m/%-d/%Y %-I:%M:%S %p",
            "datetime_short": "%-m/%-d/%Y %-I:%M %p",
            "decimal_point": ".",
            "time": "%-I:%M:%S %p",
            "time_short": "%-I:%M %p"
        },
        "name": "Zulu",
        "native_name": "isiZulu",
        "number_rule": lambda n: 'p' if not is_integral(n) else ('' if n == 1 else 'p')
    }
}