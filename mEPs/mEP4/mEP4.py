def verifyTime(age, gender):
    """
    This function returns the necessary time for classification of athlete
    """
    if gender == 'M' or gender == 'm':
        if age <= 34:
            return 180
        elif age <= 39:
            return 185
        elif age <= 44:
            return 190
        elif age <= 49:
            return 200
        elif age <= 54:
            return 205
        elif age <= 59:
            return 215
        elif age <= 64:
            return 230
        elif age <= 69:
            return 245
        elif age <= 74:
            return 260
        elif age <= 79:
            return 275
        else:
            return 290
    elif gender == 'F' or gender == 'f':
        if age <= 34:
            return 210
        elif age <= 39:
            return 215
        elif age <= 44:
            return 220
        elif age <= 49:
            return 230
        elif age <= 54:
            return 235
        elif age <= 59:
            return 245
        elif age <= 64:
            return 260
        elif age <= 69:
            return 275
        elif age <= 74:
            return 290
        elif age <= 79:
            return 305
        else:
            return 320

def formatTime(time):
    """
    This function format minutes in {xx}h {xx}min
    """
    if time < 0: time = (-1) * time
        
    hours = time // 60
    minutes = time % 60   
    return f'{format(hours, "02d")}h {format(minutes, "02d")}min'

def differenceTime(time, maxTime):
    """
    This function return the difference between time of athlet and yout category
    """
    return maxTime - time

def gotIndex(difference):
    """
    This function verify if athlete got the index and return 'SIM' or 'NAO'
    """
    if difference >=0:
        return 'SIM'
    else:
        return 'NAO'

def report(gender, time, maxTime, gotIndex, restTime):
    """
    This function show the report of the data of athlete
    """
    got = 'acima'
    if gotIndex == 'SIM': got = 'abaixo'
    
    if gender == 'F' or gender == 'f':
        print(f'Tempo da corredora: {time}')
        print(f'Tempo necessario: {maxTime}')
        print(f'Conseguiu indice? {gotIndex}')
        print(f'A corredora correu {restTime} {got} do indice')
    else:
        print(f'Tempo do corredor: {time}')
        print(f'Tempo necessario: {maxTime}')
        print(f'Conseguiu indice? {gotIndex}')
        print(f'O corredor correu {restTime} {got} do indice')

def main():
    time = int(input())
    age = int(input())
    gender = input()

    maxTime = verifyTime(age, gender)
    difference = differenceTime(time, maxTime)
    
    time = formatTime(time)
    maxTime = formatTime(maxTime)
    restTime = formatTime(difference)

    report(gender, time, maxTime, gotIndex(difference), restTime)

main()