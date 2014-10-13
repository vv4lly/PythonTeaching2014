# count poker hands

pokerFile = open("poker-hand-testing.data", 'r')
# 1. open file for reading

# 2. create and initialize variables to hold the counts
totalCount = 0
nothingCount = 0
pairCount = 0
twoPairCount = 0
threeOfaKindCount = 0
straightCount = 0
flushCount = 0
fullHouseCount = 0
fourOfaKindCount = 0
straightFlushCount = 0
royalFlushCount = 0

# 3. Loop through each line of the file
for line in pokerFile:
    totalCount = totalCount + 1  # at each line increment the counter

    # get hand rank: split on comma, get last item as int
    handRank = int(line.split(',')[-1])

    # for each type of hand, increment the appropriate counter
    if handRank == 0:
        nothingCount = nothingCount + 1
    if handRank == 1:
        pairCount = pairCount + 1
    if handRank == 2:
        twoPairCount = twoPairCount + 1
    if handRank == 3:
        threeOfaKindCount = threeOfaKindCount + 1
    if handRank == 4:
        straightCount = straightCount + 1
    if handRank == 5:
        flushCount = flushCount + 1
    if handRank == 6:
        fullHouseCount = fullHouseCount + 1
    if handRank == 7:
        fourOfaKindCount = fourOfaKindCount + 1
    if handRank == 8:
        straightFlushCount = straightFlushCount + 1
    if handRank == 9:
        royalFlushCount = royalFlushCount + 1

print("Total hands in file: ", totalCount)

print("Counts of hands: ", nothingCount, pairCount, twoPairCount, \
      threeOfaKindCount, straightCount, flushCount, fullHouseCount, \
      fourOfaKindCount, straightFlushCount, royalFlushCount)
totalCountFP = float(totalCount)  # float to force floating-point division
print("Probability:")
print(" of nothing:         %5.4f %%" % (100 * nothingCount / totalCountFP))
print(" of one pair:        %5.4f %%" % (100 * pairCount / totalCountFP))
print(" of two pairs:       %5.4f %%" % (100 * twoPairCount / totalCountFP))
print(" of three of a kind: %5.4f %%" % (100 * threeOfaKindCount / totalCountFP))
print(" of a straight:      %5.4f %%" % (100 * straightCount / totalCountFP))
print(" of a flush:         %5.4f %%" % (100 * flushCount / totalCountFP))
print(" of a full house:    %5.4f %%" % (100 * fullHouseCount / totalCountFP))
print(" of four of a kind:  %5.4f %%" % (100 * fourOfaKindCount / totalCountFP))
print(" of a straight flush:%5.4f %%" % (100 * straightFlushCount / totalCountFP))
print(" of a royal flush:   %5.4f %%" % (100 * royalFlushCount / totalCountFP))