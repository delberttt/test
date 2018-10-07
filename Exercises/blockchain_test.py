import unittest
from multiprocessing import Queue
from Exercises.week2.blockChain import Blockchain
from Exercises.week2.block import Block
from Exercises.week1.keyPair import GenerateKeyPair
from Exercises.week1.transaction import Transaction


class TestBlockchain(unittest.TestCase):
    def test_SimpleE2E(self):
        # create parties
        sender_pub, sender_priv = GenerateKeyPair()
        recv_pub, recv_priv = GenerateKeyPair()

        # create transaction2
        tx1 = Transaction(
            sender_pub,
            recv_pub,
            10,
            "First transaction"
        )
        tx2 = Transaction(
            recv_pub,
            sender_pub,
            5,
            "Return Transaction"
        )

        tx_list = [tx1, tx2]

        # create block from tx_list
        # this should be the longest step
        b = Block(tx_list)
        q = Queue(1)

        # todo: decide what to do with this
        level_of_difficulty = 3

        process = b.build(_LOD=level_of_difficulty, _book=q)
        process.start()

        # todo: create another test where interrupt possible here

        # wait for block to finish building
        process.join()

        # finish building block
        b.setNonce(q.get())

        bc = Blockchain(b)

        prev_block = b
        for i in range(3):
            b1 = Block(_transaction_list=tx_list,
                       _prev_block=prev_block,
                       _prev_header=prev_block.header)

            process = b1.build(_LOD=level_of_difficulty, _book=q)
            process.start()

            process.join()

            b1.setNonce(q.get())

            bc.addBlock(_incoming_block=b1, _prev_block=prev_block)

            prev_block = b1

        # verify
        res = bc.validate()

        self.assertEqual(
            bc.checkChainLength(bc.current_block),
            4,
            "Chain length is not 4"
        )

        self.assertTrue(res, "Validation is not True")


if __name__ == "__main__":
    unittest.main()
