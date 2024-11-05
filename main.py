# This is a sample Python script.

# Press âŒƒR to execute it or replace it with your code.
# Press Double â‡§ to search everywhere for classes, files, tool windows, actions, and settings.
numbers = {
	"0": [
		" _ ",
		"| |",
		"|_|"
	],
	"1": [
		"   ",
		"  |",
		"  |"
	],
	"2": [
		" _ ",
		" _|",
		"|_ "
	],
	"3": [
		" _ ",
		" _|",
		" _|"
	],
	"4": [
		"   ",
		"|_|",
		"  |"
	],
	"5": [
		" _ ",
		"|_ ",
		" _|"
	],
	"6": [
		" _ ",
		"|_ ",
		"|_|"
	],
	"7": [
		" _ ",
		"  |",
		"  |"
	],
	"8": [
		" _ ",
		"|_|",
		"|_|"
	],
	"9": [
		" _ ",
		"|_|",
		" _|"
	]
}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press âŒ˜F8 to toggle the breakpoint.

def parse_entry(entrada):
    return ''.join([parse_number(entrada, posicion) for posicion in range(9)])


def casilla_a_numero(casilla):
	for n, casilla_n in numbers.items():
		encontrado = True
		for c, c_n in zip(casilla, casilla_n):
			if c != c_n:
				encontrado = False
		if encontrado:
			return n

def parse_number(entrada, posicion):
    casilla = []
    for linea in entrada.split("\n"):
        posicion_ = linea[posicion * 3:posicion * 3 + 3]
        casilla.append(posicion_)
    return casilla_a_numero(casilla)


    return resultado
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


