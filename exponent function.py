print (2**3)

def raisetopower (basenum, pownum) :
    result = 1
    for index in range (pownum):
        result = result * basenum
    return result
print (raisetopower(3,4))

