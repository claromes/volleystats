# pt_BR: 'sábado, 5 de novembro de 2022 - 21:30' to 2022-11-05
# en-GB: '05 November 2022 - 21:30' to 2022-11-05

import locale
import re
from datetime import datetime

def parse_ptbr_date(str):
    str_1 = str.replace(' de ', '-')
    str_2 = str_1.replace(' ', '')
    str_3 = str_2.split(',', 1)[1]
    str_4 = str_3.rsplit('-', 1)[0]

    date_re_1 = re.search(r'-(\w+)-', str_4)
    date_re_2 = date_re_1.group(1)

    date_re_en = ''

    if date_re_2 == 'janeiro':
        date_re_en = 'january'
    elif date_re_2 == 'fevereiro':
        date_re_en = 'february'
    elif date_re_2 == 'março':
        date_re_en = 'march'
    elif date_re_2 == 'abril':
        date_re_en = 'april'
    elif date_re_2 == 'maio':
        date_re_en = 'may'
    elif date_re_2 == 'junho':
        date_re_en = 'june'
    elif date_re_2 == 'julho':
        date_re_en = 'july'
    elif date_re_2 == 'agosto':
        date_re_en = 'august'
    elif date_re_2 == 'setembro':
        date_re_en = 'september'
    elif date_re_2 == 'outubro':
        date_re_en = 'october'
    elif date_re_2 == 'novembro':
        date_re_en = 'november'
    elif date_re_2 == 'dezembro':
        date_re_en = 'december'

    var_date_re_2 = r'{}-'.format(re.escape(date_re_2))
    parsed_date = re.sub(var_date_re_2, '{}-'.format(date_re_en), str_4)

    parsed_ptbr_date = datetime.strptime(parsed_date, '%d-%B-%Y').date()

    return parsed_ptbr_date

def parse_engb_date(str):
    str_1 = str.replace(' ', '-')
    str_2 = str_1.rsplit('---', 1)[0]

    parsed_engb_date = datetime.strptime(str_2, '%d-%B-%Y').date()

    return parsed_engb_date