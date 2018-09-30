import json
import ecdsa
from .question3 import *


# variables
sender_private_key = ecdsa.SigningKey.generate(curve=ecdsa.NIST192p)
sender_public_key = sender_private_key.get_verifying_key()

receiver_private_key = ecdsa.SigningKey.generate(curve=ecdsa.NIST192p)
receiver_public_key = receiver_private_key.get_verifying_key()

amount = 10000
comment = "testRun"


# Transaction class
class Transaction:
    def __init__(self, _sender_public_key, _receiver_public_key, _amount, _comment):
        self.data = {
            "Sender": _sender_public_key.to_string().hex(),
            "Receiver": _receiver_public_key.to_string().hex(),
            "Amount": _amount,
            "Comment": _comment,
            "Signature": ""
        }

    @classmethod
    def new(cls, _from, _to, _amount, _comment, _private_key):
        # Instantiates object from passed values
        t = Transaction(_from, _to, _amount, _comment)

        # sign and return obj
        t.sign(_private_key)
        return t

    def to_json(self, _data):
        # Serializes object to JSON string
        return json.dumps(_data)

    @classmethod
    def from_json(cls, _data):
        # Instantiates/Deserializes object from JSON string
        return json.loads(_data)

    def sign(self, _private_key):
        # Sign object with private key passed
        # That can be called within new()

        # sign data with private key
        sig = signWithPrivateKey(_message=self.to_json(self.data), sk=_private_key)

        # add signature to existing data
        self.data["Signature"] = sig
        return self.data, sig

    def getVKFromData(self, _person):
        return ecdsa.VerifyingKey.from_string(bytes.fromhex(self.data[_person]))

    def validate(self):
        # Validate transaction correctness.
        # Can be called within from_json()
        # remove signature
        sig = self.data["Signature"]
        self.data["Signature"] = ""

        # verify data without signature in it
        vk = self.getVKFromData("Sender")
        result = verifyExisting(_message=self.to_json(self.data), _public_key=vk, _sig=sig)
        self.data["Signature"] = sig
        return result

    def __eq__(self, other):
        # Check whether transactions are the same
        return self.data == other.data


if __name__=="__main__":
    t = Transaction.new(sender_public_key, receiver_public_key, amount, comment, sender_private_key)
    # print(t.data)
    print(t.validate())
