
def convert_string_to_digit(digit: str):
    if digit == '-':
        return -1
    
    if digit == '=':
        return -2
    
    return eval(digit)



def convert_to_decimal(snafu: str):

    decimal = 0
    N = len(snafu) - 1
    for i in range(N, -1, -1):
        decimal += 5 ** (N - i) * convert_string_to_digit(snafu[i])
    
    #print(decimal)

    return decimal



def convert_to_snafu(decimal: int):
    snafu = ''

    while decimal != 0:
        reminder = decimal % 5
        character = ''

        if reminder <= 2:
            character = str(reminder)
        elif reminder == 3:
            character = '='
        else:
            character = '-'
    
        # add character at the beginning
        snafu = character + snafu
        decimal -= convert_string_to_digit(character)
        decimal //= 5

    return snafu



def part_one():

    total = 0
    for i in snafus:
        total += convert_to_decimal(i)
    
    print(total)
    print(convert_to_snafu(total))



# main
with open('./25/input.txt') as f:
        snafus = f.readlines()

snafus = [s.strip() for s in snafus]

part_one()