# _*_ coding: utf-8 _*_

import locale

def currency_formatter(unformated_value):
    """
    Format a number to a brazilian BRL standard.

    Formata um número para o formato padrão do BRL brasileiro.
    """
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    formatted= locale.currency(unformated_value, grouping=True, symbol=None)

    return formatted
