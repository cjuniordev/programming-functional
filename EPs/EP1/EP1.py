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
	clearTerminal()

def endMessage():
	"""
	This function show a end message for user
	"""
	clearTerminal()
	print('──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌')
	print('───▄▄██▌█░░░░ ATÉ ░░░▐.')
	print('▄▄▄▌▐██▌█░░░░ MAIS░░░▐.')
	print('███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌')
	print('▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀ ')

def showItems(amount_gpu, amount_motherboard, amount_monitor, amount_ram, amount_cpu, price_gpu, price_motherboard, price_monitor, price_ram, price_cpu):
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
	if amount_gpu > 0: print(f'|  1 - Placa de vídeo....................R${price_gpu:.2f}  |')
	if amount_motherboard > 0: print(f'|  2 - Placa Mãe.........................R${price_motherboard:.2f}  |')
	if amount_monitor > 0:print(f'|  3 - Monitor...........................R${price_monitor:.2f}  |')
	if amount_ram > 0:print(f'|  4 - Memória RAM.......................R${price_ram:.2f}  |')
	if amount_cpu > 0:print(f'|  5 - Processador.......................R${price_cpu:.2f}  |')
	print('|' + ' '*50 + '|')
	print('+' + '-'*50 + '+')
	print(RST)

def chooseOption(n):
	"""
	This function get the user option, verify if is valid and return option.

	paremeter: n = number of options | type: INT
	return type: INT
	"""
	option = int(input('--> Digite sua opção (Digite 0 para cancelar operação!): '))
	if option == 0:
		endMessage()
		exit()
	elif option < 0 or option > n:
		print(f'Opção inválida! Digite um valor entre 1 e {n}')
		option = chooseOption(n)

	return option

def confirmOption(item, price_gpu, price_motherboard, price_monitor, price_ram, price_cpu):
	"""
	Function receive id of a item and confirme option
	"""

	# colors
	RST     = '\033[00m'
	BLUE    = '\033[34m'
	GREEN   = '\033[32m'

	clearTerminal()
	
	print(BLUE)
	print('+------------------------+')
	print('|    ITEM SELECIONADO    |')
	print('+------------------------+')
	if item == 1:
		item_price = price_gpu
		print('|  Nome: Placa de vídeo  |')
		print(f'|     Preço:  {price_gpu:.2f}     |')
	elif item == 2:
		item_price = price_motherboard
		print('|    Nome: Placa mãe     |')
		print(f'|     Preço:  {price_motherboard:.2f}     |')
	elif item == 3:
		item_price = price_monitor
		print('|     Nome:  Monitor     |')
		print(f'|     Preço:  {price_monitor:.2f}     |')
	elif item == 4:
		item_price = price_ram
		print('|  Nome: Memória RAM  |')
		print(f'|     Preço:  {price_ram:.2f}     |')
	elif item == 5:
		item_price = price_cpu
		print('|   Nome:  Processador   |')
		print(f'|     Preço:  {price_cpu:.2f}     |')

	print('+------------------------+')
	
	print(GREEN)
	confirm = input('\nDeseja continuar a compra? (s/n) ')
	print(RST)
	if confirm == 's':
		return item_price
	else:
		endMessage()
		exit()
		
def payment(item_price):
	""""""
	RST     = '\033[00m'
	GREEN   = '\033[32m'
	RED     = '\033[31m'

	clearTerminal()

	print(GREEN)
	print(f'É necessaŕio R${item_price:.2f} para comprar este produto.')
	print(RST)
	insertedMoney = float(input('--> Insira aqui o valor do seu dinheiro: (Digite 0 para cancelar compra) '))

	if insertedMoney == 0:
		endMessage()
		exit()
	elif item_price <= insertedMoney:
		print('Processando pagamento...')
	else:
		clearTerminal()
		print(RED)
		print('--> Valor inserido não é suficiente para realizar esta compra!')
		print('Não tente trapecear nosso sistema!')
		print(RST)

		_ = input('\nPressione ENTER para tentar novamente. ')
		clearTerminal()

		payment(item_price)

def machine():
	"""
	Function responsible for the operation of the entire machine
	"""
	# amount
	amount_gpu = 2
	amount_motherboard = 5
	amount_monitor = 1
	amount_ram = 3
	amount_cpu = 1
	amount_options = 5

	# prices
	price_gpu = 800
	price_motherboard = 900
	price_monitor = 500
	price_ram = 300
	price_cpu = 900
	
	showItems(amount_gpu, amount_motherboard, amount_monitor, amount_ram, amount_cpu, price_gpu, price_motherboard, price_monitor, price_ram, price_cpu)
	item = chooseOption(amount_options)
	item_price = confirmOption(item, price_gpu, price_motherboard, price_monitor, price_ram, price_cpu)
	payment(item_price)


def main():
	clearTerminal()
	initialMessage()
	machine()

main()