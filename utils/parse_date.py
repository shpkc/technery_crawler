from datetime import datetime


def parse_date(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S%z')
    except ValueError:
        try:
            return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')
        except ValueError as e:
            raise ValueError(f"Unable to parse date string '{date_string}': {e}")


