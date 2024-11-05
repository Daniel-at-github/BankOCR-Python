from main import parse_entry, parse_number, casilla_a_numero
import textwrap




def kk_test_parse_entry():
    entrada = "\n".join([
        '    _  _  _  _  _  _     _ ',
        '|_||_|| || ||_   |  |  ||_ ',
        '  | _||_||_||_|  |  |  | _|',
        ''])

    salida = "490067715"
    assert parse_entry(entrada) == salida

def test_parse_number():
    entrada = "\n".join([
        '    _  _     _  _  _  _  _ ',
        '  | _| _||_||_ |_   ||_||_|',
        '  ||_  _|  | _||_|  ||_| _|',
        '                           '])

    assert parse_number(entrada, 0) == 1
    assert parse_number(entrada, 1) == 2
    assert parse_number(entrada, 10) == 9


def test_casilla_a_numero():
    entrada0 = [
		" _ ",
		"| |",
		"|_|"
	]
    entrada9 = [
		" _ ",
		"|_|",
		" _|"
	]
    assert casilla_a_numero(entrada0) == "0"
    assert casilla_a_numero(entrada9) == "9"

