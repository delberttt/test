from Exercises.week1.keyPair import GenerateKeyPair
from multiprocessing import Queue
import sys
import json
import socket



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
        self.connected_nodes = []

    @classmethod
    def new(cls, _public_key=None, _blockchain=None):
        pub_key = _public_key
        priv_kev = ""
        if _public_key is None:
            pub_key, priv_kev = GenerateKeyPair()

        m = Miner(_public_key=pub_key, _blockchain=_blockchain)

        # returns obj, public key and private key.
        return m, pub_key, priv_kev

    def addPeers(self, _peers):
        for peer in _peers:
            if peer not in self.connected_nodes:
                self.connected_nodes.append(peer)

    # connectionStart is meant to be used to "start" the Miner
    # every miner should be a server
    def connectionStart(self, _port):
        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', _port)
        print("Starting up miner server on {}...".format("localhost:", _port))
        sock.bind(server_address)

        # create queue todo: decide size of queue
        blockchain_queue = Queue(10)
        transaction_queue = Queue(10)

        while True:
            data, addrs = sock.recvfrom(4096)
            data = json.loads(data.decode())

            # todo: parse broadcast data

    def broadcastTransaction(self, _tx):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        data = json.dumps({
            "Type": "Transaction",
            "Data": str(_tx)
        })


        

    def broadcastBlock(self, _block):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        data = json.dumps({
            "Type": "Block",
            "Data": ""
        })


if __name__ == '__main__':
    pass
