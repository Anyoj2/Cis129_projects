#An actual blank


def main():
    sentinel = -1
    lowvalue = 0
    newvalue = 0
    lowestvalue = 0
    highestvalue = 0
    msg = "Enter number >"+str(lowvalue)+".Enter "+str(sentinel)+" to quit"
    newvalue = getvalidnumber(msg,lowvalue,sentinel)
    if newvalue != sentinel:
        highestvalue = newvalue
        lowestvalue = newvalue
        while newvalue != sentinel:
            if newvalue > highestvalue:
                highestvalue = newvalue
            if newvalue < lowestvalue:
                lowestvalue = newvalue
            newvalue = getvalidnumber(msg)
        print("Highest value = ",highestvalue)
        print("Lowest value = ",lowestvalue)
    else:
        print("No numbers entered")
    
def getvalidnumber(msg,lowvalue,sentinel):
    newvalue=0
    newvalue=int(input(msg))
    while newvalue < lowvalue and newvalue != sentinel:
        print("Invalid value")
        newvalue=int(input(msg))
    return newvalue
def main2():
    low = 10
    high = 100
    sentinel = -99
    newvalue = 0
    counter = 0
    msg = "Enter a odd number from"+str(low)+"-"+str(high)+","+str(sentinel)+" to quit"
    newvalue = getvalnum(msg,low,high,sentinel)
    while newvalue != sentinel:
        counter += 1
        newvalue = getvalnum(msg,low,high,sentinel)
    print(counter,"numers were entered")

def getvalnum(msg,low,high,sentinel):
    newvalue = int(input(msg))
    while isinvalid(newvalue,low,high,sentinel):
        print("Invalid value")
        newvalue = int(input(msg))
    return newvalue

def isinvalid(newvalue,low,high,sentinel):
    if newvalue == sentinel:
        return False
    if newvalue < low:
        return True
    if newvalue % 2 ==0:
        return True
    return False

main()
main2()




