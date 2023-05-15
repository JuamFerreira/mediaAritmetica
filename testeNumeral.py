def numero_ou(digito):
    """ Função que testa se o digito passado é um numeral que pode ser convertido em decimal """

    try:
        float(digito)
    except ValueError:
        return False
    return True
