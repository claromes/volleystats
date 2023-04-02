# pt_BR: 'sábado, 5 de novembro de 2022 - 21:30' to 2022-11-05
# en-GB: '05 November 2022 - 21:30' to 2022-11-05

import locale
from datetime import datetime

def parse_ptbr_date(str):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    str_1 = str.replace(' de ', '-')
    str_2 = str_1.replace(' ', '')
    str_3 = str_2.split(',', 1)[1]
    str_4 = str_3.rsplit('-', 1)[0]

    parsed_date = datetime.strptime(str_4, '%d-%B-%Y').date()

    return parsed_date

def parse_engb_date(str):
    locale.setlocale(locale.LC_ALL, 'en-GB.UTF-8')

    str_1 = str.replace(' ', '-')
    str_2 = str_1.rsplit('---', 1)[0]

    parsed_date = datetime.strptime(str_2, '%d-%B-%Y').date()

    return parsed_date