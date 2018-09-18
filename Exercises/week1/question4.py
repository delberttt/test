


class Transaction():
    def __init__(self):
        pass

    @classmethod
    def new(cls):
        pass

    def to_json(self):
        # Serializes object to JSON string
        pass

    @classmethod
    def from_json(self):
        # Instantiates/Deserializes object from JSON string
        pass

    def sign(self):
        # Sign object with private key passed
        # That can be called within new()
        pass

    def validate(self):
        # Validate transaction correctness.
        # Can be called within from_json()
        pass

    def __eq__(self, other):
        # Check whether transactions are the same
        pass


if __name__=='__main__':
    pass
