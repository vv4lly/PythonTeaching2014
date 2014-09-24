''' This program takes an integer as input and converts it to its equivalent 
in any base from 2 (binary) to 16 (hexadecimal). We impose a limit of 16 
because we don't have a convenient symbol set defined for digits beyond 15.
Hex 15 is 'f'.   

Note that even though the program is longer than the class example, most of the extra effort went on 
error trapping. 

Note also that I have partitioned the work using functions to handle the conversions and the validation 
of the base. As this validation function us invoked by both conversion functionss, this is a sensible approach.

Written by Mark Foley, October 2012 amended October 2013.
'''

baseDigits = '0123456789abcdef'


def int2base(myInt, myBase):
    ''' This function takes in an integer and a base and converts the integer to the base.
    The result is returned as a string.
    The method is to repeatedly divide the integer by the base and store the remainder.
    Example: 8 to base 2 (binary)
    1. -- 8/2 = 4, remainder 0
    2. -- 4/2 = 2, remainder 0
    3. -- 2/2 = 1, remainder 0
    4. -- 1/2 = 0, remainder 1
    5. Reading from the bottom up, answer is 1000
    '''
    print("Converting", myInt, "to", myBase)

    baseStr = ''  # Answer is initially blank
    myQuotient = myInt  # We store the quotient in myQuotient

    while myQuotient > 0:  # myQuotient reduces with each trip around the while loop until it equals 0
        baseDigit = str(baseDigits[myQuotient % myBase])  # baseDigit is the remainder converted to string
        baseStr = baseDigit + baseStr  # baseStr is prior answer added to baseDigit because the answer reads in reverse
        myQuotient //= myBase  # quotient is reduced for next trip through while loop

    print('The base', myBase, 'of', myInt, 'is', baseStr)
    return baseStr


def base2int(baseStr, myBase):
    ''' This function takes a value in string format and converts it to base 10 (decimal).
    The characters in the string must be in '0123456789abcdef'.
    The method is least significant digit * base^0 + next digit * base^1 ... and so on
    Example: 3f (base 16) = [f (15) * 16^0 = 15] + [3 * 16^1 = 48] = 63
    '''

    print("Converting", baseStr, "to decimal")

    tmpBaseStr = baseStr  # tmpBaseStr holds the string to convert less the least significant digit after each loop
    intAnswer = 0  # Answer strats at 0, is added to with each trip through the while loop
    power = 0  # Power starts at 0, increases by one for each trip through the while loop
    while len(tmpBaseStr) > 0:  # Go through string - a digit is lost each time, loop ends when there are none left
        for pos in range(len(baseDigits)):  # Look up each element in 'baseDigits'
            if baseDigits[pos] == tmpBaseStr[-1]:  # Get the integer equivalent of the current character ...
                intEquivalent = int(pos)  # ... in tmpBaseStr working from the end
                break  # Once you've found it you can stop looking
        intAnswer = intAnswer + intEquivalent * myBase ** power  # Add integer you found * the base to the power of <depends on how many trips through loop>
        tmpBaseStr = tmpBaseStr[:-1]  # String has last digit chopped off
        power += 1  # power increases by 1

    print(baseStr, 'base', myBase, 'to integer is', intAnswer)
    return intAnswer


def isValidBase(myBase):
    ''' Returns True if base is valid '''
    if not myBase.isdigit():
        print("Bad input, You must enter a valid integer")
        return False
    if int(myBase) not in range(2, 17):
        print("bad input, You must enter a number between 2 & 16")
        return False
    return True

# The program starts here.
#
# We set up a while loop that only exits when you enter '0'. 
# On each loop we get the inputs for our integer and the base. 
# Make sure that both are in valid ranges - int must be a valid number and base 
# must be between 2 & 16

optionStr = ""
while optionStr != "0":
    print("\nInteger to Base Converter")
    print("-------------------------")
    print("Choose an option")
    print("Enter 1 Convert from decimal to base x")
    print("Enter 2 Convert from base x to decimal")
    print("Enter 0 to exit the program")

    optionStr = input("Enter your choice now: ")
    if (len(optionStr) != 1) or (optionStr not in "012"):
        print("Error: You must enter a valid choice")

    #
    # This section handles Int to Base x
    #
    elif optionStr == "1":  # Int to Base selected ...
        intStr = input('Give me an integer to convert: ')

        if not intStr.isdigit():  # Invalid integer?
            print("Bad input, You must enter a valid integer")
            break

        myInt = int(intStr)  # We now have a valid integer to convert

        baseStr = input('Give me a base: ')

        if not isValidBase(baseStr):  # Invalid base?
            break

        myBase = int(baseStr)  # We now have a valid base

        myAnswer = int2base(myInt, myBase)
        print("Answer is ", myAnswer)

    #
    # This section handles Base x to Int
    #
    elif optionStr == "2":
        baseStr = input('Give me a string to convert: ')
        for char in baseStr:
            if char not in baseDigits:
                print("Bad string:", char)
                break  # ... out of 'if'
            break  # ... out of 'for' loop

        base = input('Give me a base: ')

        if not isValidBase(base):  # Invalid base?
            break

        myBase = int(base)  # We now have a valid base

        myAnswer = base2int(baseStr, myBase)
        print("Answer is ", myAnswer)

    #
    # This section causes you to exit
    #
    elif optionStr == "0":
        print("\nExiting ... Goodbye!")

    #
    # Catches any other wierd condition. Should never be reached, it's just here for completeness.
    #
    else:
        print("\Bad option")
