from Exercises.week1.helperFunctions import generateRandomString
from Exercises.week1.merkleNode import MerkleNode
from Exercises.week1.merkleTree import MerkleTree, verify_proof
import json
import time


def createAndVerify(_number):
    randomDict = {}
    sender = generateRandomString(12)
    randomDict[sender] = 1

    n = MerkleNode("Leaf", json.dumps({"Sender": sender}))
    m = MerkleTree(n)

    verify_numbers = [0, 1, 2]
    to_verify = [n]

    for i in range(_number):
        while sender in randomDict:
            sender = generateRandomString(12)

        randomDict[sender] = 1
        n1 = MerkleNode("Leaf", json.dumps({"Sender": sender}))
        m.add(n1)

        # add to verify
        if i in verify_numbers:
            to_verify.append(n1)

    print("-------------- REPORT ------------------")

    print("size of tree:", m.count_elements())
    print("total transactions:", len(m.leaf_nodes))

    # this should be true
    for i in to_verify:
        print("verification for node:", i)
        print("valid verification:", verify_proof(i, m.get_proof(i), m.root))

    # this should be false
    # print("invalid verification:",
    #       verify_proof(n, m.get_proof(n) + [MerkleNode("", json.dumps({"Sender": "attacker"}))], m.root))

    print("------------ REPORT END ----------------")


if __name__ == '__main__':
    start_time = time.time()
    createAndVerify(300)
    end_time = time.time()
    print("Total time taken:", end_time - start_time)
