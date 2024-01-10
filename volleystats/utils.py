from datetime import datetime

# '28/10/2022 - 19:30' or '28.10.2022 - 19:30' to 2022-10-28
def parse_short_date(short_date_string):
    if '/' in short_date_string:
        date_format = '%d/%m/%Y'
    elif '.' in short_date_string:
        date_format = '%d.%m.%Y'

    short_date_obj = datetime.strptime(short_date_string, f'{date_format} - %H:%M')
    parsed_short_date = short_date_obj.strftime('%Y-%m-%d')

    return parsed_short_date

# en-GB: '05 November 2022 - 21:30' to 2022-11-05
def parse_engb_date(date_string):
    str_1 = date_string.replace(' ', '-')
    str_2 = str_1.rsplit('---', 1)[0]

    parsed_engb_date = datetime.strptime(str_2, '%d-%B-%Y').date()

    return parsed_engb_date
