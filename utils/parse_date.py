from datetime import datetime

def parse_date(date_string):
    try:
        format_string = '%Y-%m-%dT%H:%M:%S%z'
        return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S%z')
    except:
        try:
            format_string = '%a, %d %b %Y %H:%M:%S %z'
            return datetime.strptime(date_string, format_string)
        except:
            try :
                format_string = '%Y-%m-%dT%H:%M:%S.%fZ'
                return datetime.strptime(date_string, format_string)
            except ValueError as e:
                raise ValueError(f"Unable to parse date string '{date_string}': {e}")


