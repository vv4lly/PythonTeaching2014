# Read file in abc music notation.

'''
X:101
T:Killavil Fancy, The
T:Eilish Brogan
T:Ten Pound Float, The
R:reel
D:Music at Matt Molloy's
D:Frankie Gavin & Alec Finn
Z:Sometimes played doubled.
Z:id:hn-reel-101
M:C|
K:G
~B3G A2BA|GE~E2 cEGE|DGBG A2BA|GEED EFGA|
~B3d A2BA|GE~E2 cEGE|DGBG A2BA|GEED ~E3D||
GABd edge|dB~B2 dBAB|GABd edge|dBAG EDB,D|
GABd edge|dB~B2 dega|(3bag ag egde|gedB AGEG||
"Variations:"
DGBG A2BA|GE~E2 cEGE|DGBG ~A3B|GEFD EGGA|
~B3d ~A3F|GE~E2 cEGE|DGBG ~A3B|GEED EGGD||
G2Bd efge|dBAB dBAB|G2Bd efge|dBAG EGGD|
G2Bd efge|dB~B2 dega|(3bag ag egde|gedB AGED||
'''
tuneCount = 0
myFile = open("hnr1.abc", "r")
for line in myFile:
    if line[:2] == "X:":
        tuneCount += 1
        hasTitle = False
        print()  # Blank line at the start of each tune
        print(line[2:-1], "...", end=' ')
    elif line[:2] == "T:":
        if not hasTitle:  # We only want the first of a possible list of titles
            print(line[2:-1], "...", end=' ')
            hasTitle = True
    elif line[:2] == "M:":
        print("Time sig:", line[2:-1], "...", end=' ')
    elif line[:2] == "K:":
        print("Key sig:", line[2:-1], "...", end=' ')

myFile.close()

print()
print("-------------------------------")
print("There are", tuneCount, "tunes in the file")
print("-------------------------------")
