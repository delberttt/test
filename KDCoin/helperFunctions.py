import random
import math
import hashlib


# generates a hex with level of difficulty depending on user
# eg. level 1 gives 0x0FFF...
# level 2 gives 0x00FFFF....
# This is a simple implementation and should not be used as a proper implementation
#   for actual generation of level of difficulty
# Can be further optimized for actual implementation
def simpleLOD(_level):
    to_return = ""
    for i in range(_level):
        to_return += "0"
    for i in range(64 - _level):
        to_return += "F"
    return int(to_return, 16)


def generateRandomString(_length):
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numString = "1234567890"
    allPossible = alphaLower + alphaUpper + numString

    toReturn = ""
    for i in range(_length):
        toReturn += random.choice(allPossible)
    return toReturn


def ceilLogBase2(_number):
    return math.ceil(math.log(_number, 2))


def hashItem(_item):
    return hashlib.sha256(str(_item).encode()).hexdigest()


