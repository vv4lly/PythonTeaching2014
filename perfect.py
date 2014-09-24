'''For a range of numbers starting at 2, determine whether the number is 'perfect', 'abundant' or 'deficient',

'''

topNum = input("What is the upper number for the range:")
topNum = int(topNum)
theNum=2
while theNum <= topNum:
    # sum up the divisors
    divisor = 1
    sumOfDivisors = 0
    while divisor < theNum:
        if theNum % divisor==0:
            sumOfDivisors = sumOfDivisors + divisor
        divisor = divisor + 1
    # classify the number based on its divisor sum
    if theNum == sumOfDivisors:
        print(theNum,"is perfect")
    elif theNum < sumOfDivisors:
        print(theNum,"is abundant")
    else:
        print(theNum,"is deficient")
    theNum += 1
