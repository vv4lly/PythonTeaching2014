# Prints decimal, character, octal and hexadecimal representation of a range of numbers
# Illustrates the representation of characters in utf-8

top_num = int(input("Enter max decimal : "))
print("| ", end="")
for dec_num in range(top_num):
    print("{} '{}' {} {} | ".format((dec_num), chr(dec_num), oct(dec_num), hex(dec_num)), end="")
    if dec_num % 3 == 0:
        print("\n| ", end="")
