

fh = open("test1.txt", "r")

for line in fh:
    print(line.strip())
    bits_of_line = line.split(" ")
    for chunk in bits_of_line:
        my_chunk = chunk
        print("PIECE: {}, ".format(chunk), end="")

