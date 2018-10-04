import hashlib
import random
import time


characters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
charUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generateRandomByteStrings():
    fullCharList = characters + numbers
    toReturn = ""
    for i in range(random.randint(1, 100)):
        choice = random.choice(fullCharList)
        toReturn += choice
    return bytes(toReturn.encode('utf-8'))

def getDigest(message):
    m = hashlib.sha512()
    m.update(message)
    return m.hexdigest()


def findCollision(numberOfBits, message):
    print("Received:", message)
    starttime = time.time()

    stringsDone = { message:1 }  # keep a list of strings already checked
    number = numberOfBits/8

    toCompare = getDigest(message)[0:int(number)]

    print("looking for", toCompare, "...")

    randomString = generateRandomByteStrings()

    while True:
        while randomString in stringsDone:
            randomString = generateRandomByteStrings()

        if getDigest(randomString)[0:int(number)] == toCompare:
            print("Found", randomString)
            print("with bytes", getDigest(randomString)[0:int(number)])
            break
        stringsDone[randomString] = 1

    # end
    endtime = time.time()
    print("Total time taken:", endtime-starttime)

    return endtime - starttime


def findPreimage(numberOfBits, message):
    starttime = time.time()

    stringsDone = { message:1 }  # keep a hashmap of strings already done
    number = numberOfBits/8

    toCompare = message

    print("looking for", toCompare, "...")

    randomString = generateRandomByteStrings()

    while True:
        while randomString in stringsDone:
            randomString = generateRandomByteStrings()

        if getDigest(randomString)[0:int(number)] == toCompare:
            print("Found", randomString)
            print("with bytes", getDigest(randomString)[0:int(number)])
            break
        stringsDone[randomString] = 1

    # end
    endtime = time.time()
    print("Total time taken:", endtime-starttime)

    return endtime - starttime


if __name__=='__main__':
    # collision for chosen string
    findCollision(40, generateRandomByteStrings())
    # pre-image
    findPreimage(32, "0000")
