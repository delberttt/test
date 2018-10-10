from KDCoin.keyPair import GenerateKeyPair


# todo: Idea is for every miner to have its own flask app
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
            priv_kev, pub_key = GenerateKeyPair()

        m = Miner(_public_key=pub_key, _blockchain=_blockchain)

        # returns obj, public key and private key.
        return m, pub_key, priv_kev

    def broadcast(self, _type, _data):
        if _type == "Block":
            pass
        elif _type == "Transaction":
            pass


if __name__ == '__main__':
    pass
