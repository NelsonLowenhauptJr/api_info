# _*_ coding: utf-8 _*_

import locale

def currency_formatter(unformated_value):
    """
    Format a number to a brazilian BRL standard.

    Formata um número para o formato padrão do BRL brasileiro.
    """

    formatted= '{:,.2f}'.format(unformated_value)
    formatted= formatted.replace(',','*')
    formatted= formatted.replace('.',',')
    formatted= formatted.replace('*','.')

    return formatted
