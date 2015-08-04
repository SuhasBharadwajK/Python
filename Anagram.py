import math

def nCr(n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

testCases = int(raw_input())

for testCase in range(testCases):
    
    inputString = raw_input()

    subStringList = list()
    count = 0
    stringCount = dict()
    occurances = dict()

    for i in range(len(inputString)):
        for j in range(i, len(inputString)):
            currentString = inputString[ i : j + 1 ]
            if currentString != inputString:
                #print currentString
                subStringList.append(currentString)

    #print subStringList

    for string in subStringList:
        if string in stringCount:
            stringCount[string] += 1
        else:
            stringCount[string] = 1
        if len(string) > 1:
            occurances[string] = dict()

    for string in stringCount:
        if len(string) == 1:
            #None
            print string + " " + str(stringCount[string])
    #print occurances

    for string in stringCount:
        if stringCount[string] > 1:
            #None
            #count += stringCount[string]%2 + 1
            count += nCr(stringCount[string], 2)

    for string in stringCount:
        if len(string) > 1:                
            for char in string:
                if char in occurances[string]:
                    occurances[string][char] += 1
                else:
                    occurances[string][char] = 1

    #print occurances

    for string1 in occurances:
        if string1 == {}:
            continue
        for string2 in occurances:
            if occurances[string1] == occurances[string2] and string1 != string2:
                if occurances[string2] != {}:
                    count += 1
                    occurances[string2] = dict()
        occurances[string1] = dict()

    print count
