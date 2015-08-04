def funct(num):
    yield num
    for x in funct(num+1):
        if num <= 100:
            yield x

print list(funct(1))
