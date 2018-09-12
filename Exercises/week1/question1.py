import hashlib

toHash = b"Blockchain Technology"

def sha2hashWord256():
    m = hashlib.sha256()
    m.update(toHash)
    return m.hexdigest()

def sha2hashWord512():
    m = hashlib.sha512()
    m.update(toHash)
    return m.hexdigest()

def sha3hashWord256():
    m = hashlib.sha3_256()
    m.update(toHash)
    return m.hexdigest()

def sha3hashWord512():
    m = hashlib.sha3_512()
    m.update(toHash)
    return m.hexdigest()

if __name__ == '__main__':
    listOfFunctions = [sha2hashWord256(),sha2hashWord512(),sha3hashWord256(),sha3hashWord512()]
    for functions in listOfFunctions:
        print(functions)
