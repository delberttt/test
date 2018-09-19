import json
import ecdsa
from question3 import *

# This is the data, d
class Transaction:
    def __init__(self, _sender, _receiver, _amount, _comment):
        self.data = {
            "Sender": _sender,
            "Receiver": _receiver,
            "Amount": _amount,
            "Comment": _comment,
            "Signature": "",
        }
        self.jsonForm = ""

    @classmethod
    def new(cls):
        # takes in a private key and signs the object with it, discarding after
        pass

    def to_json(self):
        # Serializes object to JSON string
        self.jsonForm = str(self.data)
        return self.jsonForm

    @classmethod
    def from_json(self, _jsonBlock):
        # Instantiates/Deserializes object from JSON string
        self.data = json.loads(_jsonBlock)
        return self.data

    def sign(self, _private_key):
        # Sign object with private key passed
        # That can be called within new()
        sig, vk = signWithPrivateKey(self.to_json(), _private_key)
        self.data['Signature'] = sig
        return self.to_json(), vk

    def validate(self, _transaction):
        # Validate transaction correctness.
        # Can be called within from_json()
        data = json.loads(_transaction)

        public_key = data['Sender']
        sig = _transaction['Signature']

        # extract signature
        _transaction["Signature"] = ""
        toVerify = str(_transaction)

        # verify with public key
        return verifyExisting(toVerify, public_key, sig)


    def __eq__(self, other):
        # Check whether transactions are the same
        # If you're using this, you're wrong
        return False


if __name__=='__main__':
    t = Transaction("clemence", "gio", "10 000", "test")
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    data, vk = t.sign(sk)
    print(t.validate(data))

