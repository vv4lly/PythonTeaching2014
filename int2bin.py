''' Simple program to convert integers to binary and vice versa

Mark Foley October 2013
'''

print('Int to binary')
intStr = input('Give me an int: ')
myInt = int(intStr)

binStr = ''
while myInt > 0:
    binStr = str(myInt % 2) + binStr
    myInt //= 2

print('The binary of', intStr, 'is', binStr)

print('\nBinary to int')
binStr = input('Give me a binary string: ')

temp = binStr
newInt = 0
power = 0
while len(temp) > 0:
    bit = int(temp[-1])
    newInt = newInt + bit * 2 ** power
    temp = temp[:-1]
    power += 1

print(binStr, 'to integer is', newInt)