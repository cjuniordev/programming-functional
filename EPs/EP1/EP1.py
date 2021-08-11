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
	"""
	This function show a welcome message for user
	"""
	VIOLET  = '\033[35m'
	print(VIOLET)
	print('#'*52)
	print('#  ------- Bem vindo à máquina de vendas  -------  #')
	print('#' + ' '*50 + '#')
	print('#  Essa máquina vende componentes de computadores  #')
	print('#' + ' '*50 + '#')
	print('#     ------- Criado por Carlos Junior -------     #')
	print('#'*52 + '\n')
	
	GREEN   = '\033[32m'
	print(GREEN)
	_ = input('Caso tenha interesse em continuar utilizando a máquina, pressione ENTER.')

def showItems(gpu, motherboard, monitor, ram, cpu):
	"""
	This function show which products they are availables to sale with her prices and amount
	"""
	RST     = '\033[00m'
	BLUE    = '\033[34m'
	print(BLUE)
	print('+' + '-'*50 + '+')
	print('|' + ' '*50 + '|')
	print('|                MÁQUINA DE VENDAS                 |')
	print('|               ESCOLHA UM PRODUTO                 |')
	print('|' + ' '*50 + '|')
	print('+' + '-'*50 + '+')
	print('|' + ' '*50 + '|')
	if gpu > 0: print('|  1 - Placa de vídeo....................R$800,00  |')
	if motherboard > 0: print('|  2 - Placa Mãe.........................R$900,00  |')
	if monitor > 0:print('|  3 - Monitor...........................R$500,00  |')
	if ram > 0:print('|  4 - Memória RAM.......................R$300,00  |')
	if cpu > 0:print('|  5 - Processador.......................R$900,00  |')
	print('|' + ' '*50 + '|')
	print('+' + '-'*50 + '+')
	print(RST)


def machine():
	"""
	Function responsible for the operation of the entire machine
	"""
	gpu = 2
	motherboard = 5
	monitor = 1
	ram = 3
	cpu = 1
	showItems(gpu, motherboard, monitor, ram, cpu)


def main():
	clearTerminal()
	initialMessage()
	clearTerminal()
	machine()

main()