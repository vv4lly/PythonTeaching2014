'''
prompt for a number
for the number, collect all the factors
once collected, sum up the factors
compare the sum and the number and
respond accordingly
'''

my_num = input("enter num: ")
my_int = int(my_num)

start_factor = 1
tot_factors = 0

while start_factor < my_int:
    if my_int % start_factor == 0:
        tot_factors += start_factor
    start_factor += 1

if my_int == start_factor:
    print("{} is perfect".format(my_int))
else:
    print("{} is NOT perfect".format(my_int))

