# taking data
weight = float(input())
age = int(input())
if 16 <= age < 18:
    doc_authorization = input()  

good_health = input()
use_injetables_drugs = input()  
first_donate = input()

if first_donate == 'N':
    months_since_last_donate = int(input())
    donate_in_last_year = int(input())

biologic_sex = input()

if biologic_sex == 'F':
    pregnancy = input()
    breastfeeding = input()
    if breastfeeding == 'S':
        age_of_baby = int(input())

# output of data
print(f'Peso: {weight}')
print(f'Idade: {age}')
if 16 <= age < 18:
    print(f'Documento de autorizacao: {doc_authorization}')  

print(f'Boa saude: {good_health}')
print(f'Uso drogas injetaveis: {use_injetables_drugs}')  
print(f'Primeira doacao: {first_donate}')

if first_donate == 'N':
    print(f'Meses desde ultima doacao: {months_since_last_donate}')
    print(f'Doacoes nos ultimos 12 meses: {donate_in_last_year}')

print(f'Sexo biologico: {biologic_sex}')

if biologic_sex == 'F':
    print(f'Gravidez: {pregnancy}')
    print(f'Amamentando: {breastfeeding}')
    if breastfeeding == 'S':
        print(f'Meses bebe: {age_of_baby}')

# verify impediments

## flags
valid_weight = True
valid_age = False
valid_health = True
valid_use_drugs = True
valid_interval = True
max_donates = False
is_pregancy = False
is_breastfeeding = False

if weight < 50:
    valid_weight = False
    print('Impedimento: abaixo do peso minimo.')
if age < 16:
    print('Impedimento: menor de 16 anos.')
elif 16 <= age < 18 and doc_authorization == 'N':
    print('Impedimento: menor de 18 anos, sem consentimento dos responsaveis.')
elif age > 60 and age < 69 and first_donate == 'S':
    print('Impedimento: maior de 60 anos, primeira doacao.')
elif age > 69:
    print('Impedimento: maior de 69 anos.')
else:
    valid_age = True

if good_health == 'N':
    valid_health = False
    print('Impedimento: nao esta em boa saude.')

if use_injetables_drugs == 'S':
    valid_use_drugs = False
    print('Impedimento: uso de drogas injetaveis.')

if biologic_sex == 'M':
    if first_donate == 'N':
        if months_since_last_donate < 2:
            valid_interval = False
        if donate_in_last_year >= 4:
            max_donates = True
            
elif biologic_sex == 'F':
    if first_donate == 'N':
        if months_since_last_donate < 3:
            valid_interval = False
        if donate_in_last_year >= 3:
            max_donates = True
    if pregnancy == 'S':
        is_pregancy = True
    if breastfeeding == 'S':
        if age_of_baby < 12:
            is_breastfeeding = True
            
## verify flags
if not valid_interval:
    print('Impedimento: intervalo minimo entre as doacoes nao foi respeitado.')
if max_donates:
   print('Impedimento: numero maximo de doacoes anuais foi atingido.')
if is_pregancy:
    print('Impedimento: gravidez.')
if is_breastfeeding:
    print('Impedimento: amamentacao.')

# if all is valid
if valid_weight and valid_age and valid_health and valid_use_drugs and valid_interval and not max_donates and not is_pregancy and not is_breastfeeding:
    print('Procure um hemocentro.')