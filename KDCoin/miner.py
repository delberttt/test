from keyPair import GenerateKeyPair
import blockChain, block, transaction


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

        # if this is ever invoked, it must be the first block
        # of the first miner
        if self.blockchain is None:
            # create new blockchain with empty data
            self.blockchain = blockChain.Blockchain(
                block.Block(
                    _transaction_list=[
                        # initial empty transaction
                        transaction.Transaction(
                            self.address,
                            self.address,
                            self.balance,
                            "Init Tx"
                        )
                    ]
                )
            )

    def broadcast(self, _type, _data):
        if _type == "Block":
            pass
        elif _type == "Transaction":
            pass


if __name__ == '__main__':
    pass
