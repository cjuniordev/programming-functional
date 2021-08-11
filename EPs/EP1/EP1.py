from os import system, name

""" Machine of sales 

	This machine sales hardware components.
	Components:
	- Graphics Card
	- Motherboard
	- Monitor
	- RAM memory
	- CPU

	Simulate a machine, receive a value and return change in notes and coins.
	- Change with a minimum number of notes and coins.
	- When the product is out of stock, show some unavailable product message or don't show it in the product list.

	Example of change(R$0,24):
		R$0,10
		R$0,10
		R$0,01
		R$0,01
		R$0,01
		R$0,01
"""

""" colors
# RST     = '\033[00m'
# GRAY    = '\033[30m'
# RED     = '\033[31m'
# GREEN   = '\033[32m'
# YELLOW  = '\033[33m'
# BLUE    = '\033[34m'
# VIOLET  = '\033[35m'
# CYAN    = '\033[36m'
# WHITE   = '\033[37m'
print(BLUE)
"""

def clearTerminal(): 
	"""
	This function is responsible for clear terminal based on kernel of SO.
	"""
	if name == 'nt':  # Windows
		system('cls') 
	else:  # Kernel Linux e outros
		system('clear') 

def initialMessage():
	BLUE    = '\033[34m'
	print(BLUE)
	print('###############################################\n')
	print('------- Bem vindo à máquina de vendas  -------\n')
	print('Essa máquina vende componentes de computadores\n')
	print('  ------- Criado por: Carlos Junior -------\n')
	print('###############################################\n')
	_ = input('Caso tenha interesse em continuar utilizando a máquina, pressione ENTER.')

#def machine():


def main():
	clearTerminal()
	initialMessage()

main()