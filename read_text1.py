# Sample program to read line by line from a text file
# and split each line into chunks

fh = open("test1.txt", "r")

for line in fh:
    print(line.strip())
    bits_of_line = line.split(" ")
    for chunk in bits_of_line:
        my_chunk = chunk
        print("PIECE: {}, ".format(chunk), end="")

