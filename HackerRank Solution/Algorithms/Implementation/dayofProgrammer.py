def dayOfProgrammer(year):  
    if ((year <= 1917) and (year % 4 == 0)) or ((year >= 1919) and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
        print('12.09.{}'.format(year))
    elif (year == 1918):
        print('26.09.{}'.format(year))
    else:
        print('13.09.{}'.format(year))
if __name__ == '__main__':
    year = int(input())
    result = dayOfProgrammer(year)
