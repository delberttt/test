from Exercises.week1.keyPair import generateVerifyKeyPairs


# todo:
# Miner's capabilities:
# - contains list of transactions
# - contains Blockchain
# - Ability to add blocks to the chain automatically
#   - Should automatically reward himself if he's the first to find
# - Ability to broadcast new block/ interrupt if broadcast received
# - Keeping track of balance is done either through UTXO or account balance
# - How to verify transaction?
class Miner:
    def __init__(self, _public_key, _blockchain=None):
        # create new miner with fields:
        self.blockchain = _blockchain
        self.tx_list = []
        self.balance = 0
        self.address = _public_key

    @classmethod
    def new(cls, _public_key=None, _blockchain=None):
        pub_key = _public_key
        priv_kev = ""
        if _public_key is None:
            pub_key, priv_kev = generateVerifyKeyPairs()

        m = Miner(_blockchain, pub_key)

        # returns obj, public key and private key.
        return m, pub_key, priv_kev


if __name__ == '__main__':
    pass
