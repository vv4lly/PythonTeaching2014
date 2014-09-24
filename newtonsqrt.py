# Newton's Method to calculate square root

# get three inputs from the user (two ints, 1 float)
num_str = input("Find the square root of integer: ")
while not num_str.isdigit():
       print("Pay attention")
       num_str = input("Find the square root integer: ")
number_int = int(num_str)

guess_str = input("Initial guess: ")
while not guess_str.isdigit():
       print("Pay attention")
       guess_str = input("Initial guess: ")
guess_float= float(guess_str)

originalGuess_float = guess_float # hang onto the original guess
count_int = 0                     # count the number_int of guesses

# get the float tolerance, no checking of input!
tolerance_float = float(input("What tolerance :"))

# do the algorithm steps as described above
previous_float = 0
count_int = 0
while abs(previous_float - guess_float) > tolerance_float:
       previous_float = guess_float
       quotient = number_int/guess_float
       guess_float= (quotient+guess_float)/2
       count_int = count_int + 1

# output the three original values, the num_int of
# iterations and the square root
print("Square root of",number_int," is: ",guess_float)
print("Took ",count_int," reps to get it to tolerance: ",tolerance_float)
print("Starting from a guess of: ", originalGuess_float)
