maximum = int(raw_input())

database = dict()
tempbase = dict()
squareSum = 0
numberOf89s = 0
iterations = 0

def funct(num):
    global iterations
    iterations += 1
    summ = 0
    global database
    global tempbase
    global numberOf89s

    '''if num in database:
        numberOf89s += 1
        return True'''

    while num != 0:
        summ += (num%10)**2
        num = num/10
    if summ == 89:
        numberOf89s += 1
        return True
    elif summ == 1:
        return False
    else:
        if summ not in database:
            tempbase[summ] = 1

        if funct(summ):
            database = dict(database.items() + tempbase.items());
        else:
            tempbase = dict()


#number = maximum
#summ = 0
#numberOf89s = 0

'''while number != 0:
    summ += (number%10)**2
    number = number /10'''

#print summ

for i in range(2, maximum):
    funct(i)
    '''while number != 89 and number != 1:
    
        while number != 0:
            squareSum += (number%10)**2
            number /= 10
    
        if squareSum == 1:
            break

        
        if squareSum in database:
            break
        ''else:
            database[squareSum] = 1''

        number = squareSum
        print number
        #print database
        squareSum = 0

    #print number
    if number == 89:
        numberOf89s += 1'''
        

#print str(number) + " Final"
print numberOf89s
print database
print iterations
