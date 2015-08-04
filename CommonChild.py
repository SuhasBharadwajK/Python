string1 = raw_input()
string2 = raw_input()

list1 = list(string1)
list2 = list(string2)
tempList = list() #Not used
countList = [0]*5000
orderList = list()

totalCount = 0 #Not used
count = 0 #Debug use
auxCount = 0 #Not used
insertFlag = 0 #Not used
lastChar = "" #Not used

lastOccurance = dict() #Not used
countDict = dict() #Not used

tempDict = dict()

'''if len(list1) < len(list2) or True:
    temp = list2
    list2 = list1
    list1 = temp'''

for char in list1:
    count += 1
    print "Iteration number: " + str(count)
    if char in list2:
        tempDict = dict()
        tempDict[char] = list2.index(char)
        print "Current character index = " + str(tempDict[char])
        print ''.join(list2)
        print list2
        #list2.pop(tempDict[char])
        list2[tempDict[char]] = ""
        #print char + " " + str(tempDict[char])
        '''if char not in lastOccurance:
            tempDict[char] = list2.index(char)
            list2.pop(tempDict[char])
        else:            
            tempDict[char] = list2[lastOccurance[char] + 1 : ].index(char)'''
        if len(orderList) == 0: #For the first iteration
            orderList.append(tempDict)            
            #print orderList
            #print "Firsted"
            #list2.pop(tempDict[char])
            #tempDict = dict()
            #tempDict[char] = list2.index(char)
            #lastChar = char
        else: #For the next iterations, when the list is not empty.
            #insertFlag = 0
            for order in orderList: #Pick a dictionary from the list of them
                #insertFlag = 0
                #print orderList
                if char not in order: #The current character is not in the current dictionary
                    if tempDict[char] > max(order.values()):
                        print "Inserted " + char  +  " into required dicts in order list"
                        orderList[orderList.index(order)][char] = tempDict[char] #Put th
                        #list2.pop(tempDict[char])
                        #insertFlag = 1
                    else: #The current character's behind the farthest element seen so far
                        if orderList.index(order) + 1 == len(orderList):
                            orderList.append(tempDict) #Create a new dictionary
                            print "The element " + char + " wasn't suitable in any dict. Appending to the list."
                            break
                            #print "Appended"
                        else:
                            continue
                    #break #Now that the char is inserted, break the loop.
                else: #The current character is already in the current dictionary
                    #if char in list2[tempD
                    currentIndex = orderList.index(order)
                    countList[currentIndex] += 1
                    print char + " already exists. Incrementing count at " + str(currentIndex)
                    #tempDict[char] = list2.index(char)
                    orderList[currentIndex][char] = tempDict[char]
        #lastOccurance[char] = tempDict[char]
    print
    print

'''
            if char not in orderDict:
                if orderDict[lastChar] > list2.index(char):
                   # orderDict.pop(lastChar)
                   # print "Popped" + char
                   orderDict = dict()
                   countList.append(auxCount)
                   auxCount = 0

                orderDict[char] = list2.index(char)
                lastChar = char
                auxCount += 1

            else:
                if list2.index(char) > orderDict[lastChar]:
                    if char not in countDict:
                        countDict[char] = 1
                    else:
                        countDict[char] += 1

                orderDict[char] = list2.index(char)
                lastChar = char
                auxCount += 1
#            if list2.index(char) == len(list2) - 1:
#                break
            '''


#totalCount += len(orderDict)
#print totalCount
#print orderDict
#print countDict
#for count in countDict.values():
#    totalCount += count

#print totalCount
#print max(countList)
#print ''.join(list1)
#print ''.join(list2)
if len(orderList) != 0:
    print max(orderList)
    print orderList
    #print countList[orderList.index(max(orderList))]
    print str(len(max(orderList))) + " " + str(orderList.index(max(orderList))) + " The longest"
    for i in countList:
        if i != 0:
            print str(i) + " " + str(countList.index(i)) + ": The count array"
    print len(max(orderList)) + countList[orderList.index(max(orderList))]    
else:
    print 0
