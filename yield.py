n = 0
def rekurse(z):
    global n
    if z:
        yield z
        for x in rekurse(z-1):
            n += 1
            yield x

print list(rekurse(14))
print n
