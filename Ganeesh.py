inputGrid = list()

for i in range(9):
    inputGrid.append(raw_input())


indices = list()

for line in inputGrid:

    total = 0

    indices.append(list(line).index('0'))
    lineList = list(line)
    for char in lineList:
        total += int(char)

    lineList[lineList.index('0')] = str(45 - total)
    print ''.join(lineList)
