from main import parse_entry, parse_number
import textwrap
def kk_test_parse_entry():
    entrada = "\n".join([
        '    _  _     _  _  _  _  _ ',
        '  | _| _||_||_ |_   ||_||_|',
        '  ||_  _|  | _||_|  ||_| _|',
        '                           '])
    salida = "123456789"
    assert parse_entry(entrada) == salida

def test_parse_number():
    entrada = "\n".join([
        '    _  _     _  _  _  _  _ ',
        '  | _| _||_||_ |_   ||_||_|',
        '  ||_  _|  | _||_|  ||_| _|',
        '                           '])


    salida = "1"
    assert parse_number(entrada, 0) == 1
    assert parse_number(entrada, 1) == 2
    assert parse_number(entrada, 10) == 9
