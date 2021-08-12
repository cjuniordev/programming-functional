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
	return None
	"""
	if name == 'nt':
		system('cls') 
	else:
		system('clear') 

def initialMessage():
	"""
	This function show a welcome message for user.
	return None
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
	This function show a end message for user.
	return None
	"""
	clearTerminal()
	print('──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌')
	print('───▄▄██▌█░░░░ ATÉ ░░░▐.')
	print('▄▄▄▌▐██▌█░░░░ MAIS░░░▐.')
	print('███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌')
	print('▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀ ')

def showItems(amount_gpu, amount_motherboard, amount_monitor, amount_ram, amount_cpu, price_gpu, price_motherboard, price_monitor, price_ram, price_cpu):
	"""
	This function show which products they are availables to sale with her prices and amount.

	paremeters:
	- amount_{product} = amount of product available | type: INT.
	- price_{product} = price of product | type: NUMBER(any).

	return None
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
	return n: INT
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
	Function receive id of a item and confirme option.

	paremeter:
	- item = id of item | type: INT.
	- price_{product} | type: NUMBER(any).

	return item_price: NUMBER(any).
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
	"""
	This function is a payment system, manages values, receives payment and calls change function.

	parameter: item_price = price of item | type: NUMBER(any).

	return None.
	"""
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
		change(insertedMoney, item_price)
	else:
		clearTerminal()
		print(RED)
		print('--> Valor inserido não é suficiente para realizar esta compra!')
		print('Não tente trapecear nosso sistema!')
		print(RST)

		_ = input('\nPressione ENTER para tentar novamente. ')
		clearTerminal()

		payment(item_price)

def calculateNotesCoinsInReal(real):
	"""
	This function receives the total change in R$ and calculate amount notes and coins in R$(100, 50, 20, 10, 5, 2 and 1) is necessary.

	parameter: real = total change in real | type: INT.

	return
	- real100 | type: INT,
	- real50  | type: INT, 
	- real20  | type: INT, 
	- real10  | type: INT,
	- real5   | type: INT, 
	- real2   | type: INT, 
	- real1   | type: INT.
	"""
	real100 = real // 100
	rest = real % 100
	real50 = rest // 50
	rest = rest % 50
	real20 = rest // 20
	rest = rest % 20
	real10 = rest // 10
	rest = rest % 10
	real5 = rest // 5
	rest = rest % 5
	real2 = rest // 2
	rest = rest % 2
	real1 = rest

	return real100, real50, real20, real10, real5, real2, real1

def calculateCoinsInCents(cents):
	"""
	This function receives the total change in cents and calculate amount coins in cents(50, 25, 10, 5 and 1)
	is necessary.

	parameter - cents = total change in cents | type: INT.

	return
	- cents50 | type: INT, 
	- cents25 | type: INT,
	- cents10 | type: INT, 
	- cents5  | type: INT, 
	- cents1  | type: INT.
	"""
	cents50 = cents // 50
	rest = cents % 50
	cents25 = rest // 25
	rest = rest % 25
	cents10 = rest // 10
	rest = rest % 10
	cents5 = rest // 5
	rest = rest % 5
	cents1 = rest

	return cents50, cents25, cents10, cents5, cents1

def printValue(value, amount):
	"""
	Receive value of note or coin and print 'R${value}' {amount} times.

	parameters
	- value | type: NUMBER(any),
	- amount | type: INT.

	return None
	"""
	if amount > 0:
		print(f'R${value:.2f}')
		printValue(value, amount - 1)

def printChangeReal(real100, real50, real20, real10, real5, real2, real1):
	"""
	This function verify which 'reals' is necessary to print.

	parameters
	- real100 | type: INT, 
	- real50  | type: INT, 
	- real20  | type: INT, 
	- real10  | type: INT, 
	- real5   | type: INT, 
	- real2   | type: INT, 
	- real1   | type: INT.

	return None
	"""
	if real100 != 0:
		printValue(100, real100)
	if real50 != 0:
		printValue(50, real50)
	if real20 != 0:
		printValue(20, real20)
	if real10 != 0:
		printValue(10, real10)
	if real5 != 0:
		printValue(5, real5)
	if real2 != 0:
		printValue(2, real2)
	if real1 != 0:
		printValue(1, real1)

def printChangeCents(cents50, cents25, cents10, cents5, cents1):
	"""
	This function verify which 'cents' is necessary to print.

	parameters
	- cents50 | type: INT, 
	- cents25 | type: INT, 
	- cents10 | type: INT, 
	- cents5  | type: INT, 
	- cents1  | type: INT.

	return None
	"""

	if cents50 != 0:
		printValue(0.50, cents50)
	if cents25 != 0:
		printValue(0.25, cents25)
	if cents10 != 0:
		printValue(0.10, cents10)
	if cents5 != 0:
		printValue(0.05, cents5)
	if cents1 != 0:
		printValue(0.01, cents1)

def calculateMinimumChange(change):
	"""
	This function receive change to give back, separate real and cents, calculate amount notes/coins and print it.

	parameter: change | type: NUMBER(any).

	return None
	"""
	real = int(change) # give integer change
	cents = int((change - real)*100) # give decimal change and transform to integer
	
	real100, real50, real20, real10, real5, real2, real1 = calculateNotesCoinsInReal(real)
	cents50, cents25, cents10, cents5, cents1 = calculateCoinsInCents(cents)

	printChangeReal(real100, real50, real20, real10, real5, real2, real1)
	printChangeCents(cents50, cents25, cents10, cents5, cents1)

def change(receive_money, item_price):
	"""
	This function generate change of payment.

	parameters:
	- receive_money | type: NUMBER(any),
	- item_price    | type: NUMBER(any).

	return None
	"""

	change = receive_money - item_price
	if change == 0:
		print(f'R${change:.2f}') # remove this line, if change == 0, return thing.
	else:
		calculateMinimumChange(change)


def machine():
	"""
	Function responsible for the operation of the entire machine.
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