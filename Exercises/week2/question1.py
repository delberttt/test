from Exercises.week1 import question5, question4
import time
import json
import ecdsa


# Block should be used until a set number of transactions are complete
# Thereafter, automatically adds itself to Blockchain
class Block:
    def __init__(self, _prev=None, _nonce=None, _root=None, _timestamp=time.time()):
        self.timestamp = _timestamp  # timestamp of block
        self.prev = _prev  # hash of previous header
        self.nonce = _nonce  # random number needed to generate PoW
        self.root = _root  # root of the hash tree
        self.default_root = False  # bool check if this is empty Block
        self.prev_block = None
        self.merkle_tree = None

        # check if root has been initialised
        if _root is None:
            # create merkle node
            default_node = question5.MerkleNode(_type="Leaf", _transaction="fake")

            # create merkle tree
            t = question5.MerkleTree(_node=default_node)

            self.merkle_tree = t
            self.root = t.root
            self.default_root = True
        else:
            self.merkle_tree = question5.MerkleTree(_node=_root)

    # adds to data within the block, insecure as question does not require "signing"
    def add(self, _sender_public_key, _receiver_public_key, _amount, _comment):
        t = question4.Transaction(_sender_public_key, _receiver_public_key, _amount, _comment)
        node = question5.MerkleNode(_type="Leaf", _transaction=json.dumps(t.data))

        if self.default_root:  # default root in use, replace.
            self.merkle_tree = question5.MerkleTree(_node=node)
            self.root = node
            self.default_root = False
        else:
            self.merkle_tree.add(_node=node)

    # validate the tree, unknown number of checks needed
    def validate(self):
        conditions = [
            self.root is not None,  # verify root is not None
            not self.default_root,  # verify not default root
                      ]

        for condition in conditions:
            if not condition:
                return False
        return True

    # _prev here should be a Block
    def setPrevBlock(self, _prev):
        self.prev_block = _prev
        # prev is a hash contained within the node in the tree
        self.prev = _prev.root.data["Transaction"]


# Blockchain contains the current block, as well as the previous block
class Blockchain:
    def __init__(self, _block=Block()):
        self.current_block = _block

    def validate(self):
        # check root
        if self.current_block is None:
            return False

        current_block = self.current_block

        # validate all blocks prior
        while current_block is not None:
            if not current_block.validate():
                return False
            current_block = current_block.prev_block

        return True

    # adds a new block
    def addBlock(self, _block):
        # set current block as the prev block
        _block.setPrevBlock(self.current_block)

        # set current block
        self.current_block = _block

    # add a transaction to current block
    def addTransaction(self, _sender_public_key, _receiver_public_key, _amount, _comment):
        self.current_block.add(_sender_public_key, _receiver_public_key, _amount, _comment)

    # Question 2
    def resolve(self):
        # resolves longest chain
        pass


if __name__ == '__main__':
    sender_private_key = ecdsa.SigningKey.generate(curve=ecdsa.NIST192p)
    sender_public_key = sender_private_key.get_verifying_key()

    receiver_private_key = ecdsa.SigningKey.generate(curve=ecdsa.NIST192p)
    receiver_public_key = receiver_private_key.get_verifying_key()

    amount = 10000
    comment = "testRun"

    bc = Blockchain()
    bc.addTransaction(sender_public_key, receiver_public_key, 200, "TestAmount")
    print(bc.current_block.root)

