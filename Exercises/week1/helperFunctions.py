import random
import math
import hashlib


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


