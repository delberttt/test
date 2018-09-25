import ecdsa


# sk is private key, vk is public key
def generateSig(_message):
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    sig = sk.sign(_message.encode('utf-8'))
    return sig, vk


def signWithPrivateKey(_message, sk):
    sig = sk.sign(_message.encode('utf-8'))
    return sig


def verifyExisting(_message, _public_key, _sig):
    return _public_key.verify(_sig, _message.encode('utf-8'))  # True


def generateVerifyKeyPairs():
    message = "Blockchain Technology"
    sig, vk = generateSig(message)
    # return vk.verify(sig, message.encode('utf-8'))
    return verifyExisting(message, vk, sig)

if __name__=='__main__':
    print(generateVerifyKeyPairs())
