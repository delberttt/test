import hashlib
import json
import math
import random


def generateRandomString(_length):
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numString = "1234567890"
    allPossible = alphaLower + alphaUpper + numString

    toReturn = ""
    for i in range(_length):
        toReturn += random.choice(allPossible)
    return toReturn


def ceilLogBase2(_number):
    return math.ceil(math.log(_number, 2))


def hashItem(_item):
    return hashlib.sha256(str(_item).encode()).hexdigest()


############
# MerkleNode
# This is a node containing the type and the transaction, in hex
# Also contains pointers to other nodes
############
class MerkleNode:
    def __init__(self, _type, _transaction):
        self.data = {
            "Type": _type,
            "Transaction": hashItem(_transaction)
        }
        self.parent = None
        self.children = [None, None]

    def findPartner(self):
        if self.parent is None:
            return None
        for child in self.parent.children:
            if child is not self:
                return child
        return None

    def setParent(self, _node):
        self.parent = _node

    def setChild(self, _position, _node):
        self.children[_position] = _node

    def hasChildren(self):
        if self.children[0] is None and self.children[1] is None:
            return False
        return True

    def hasParent(self):
        if self.parent is None:
            return False
        return True

    def __str__(self):
        return json.dumps(self.data)


# destroy connections to parent and delete object
def destroyParentConnection(_node):
    # wipe node
    _node.parent.children = []
    _node.parent.parent = None

    # delete object
    obj = _node.parent
    _node.parent = None
    del obj


# meant to be used by last Merkle node to get left nodes
def getLeftNodes(_node):
    arr = []
    current_node = _node
    while current_node.parent is not None and current_node.parent is not current_node:
        arr.append(current_node.parent.children[0])
        current_node = current_node.parent

    return arr


def createNewNode(_merging_node, _incoming_node):
    new_transaction = hashItem(_merging_node.data["Transaction"] + _incoming_node.data["Transaction"])

    n = MerkleNode("", new_transaction)
    n.setChild(0, _merging_node)
    n.setChild(1, _incoming_node)
    _merging_node.setParent(n)
    _incoming_node.setParent(n)

    # print("NEW NODE CREATED:\nParent: {}\nleft: {}\nright: {}\n\n".format(n.parent, n.children[0], n.children[1]))

    return n


def buildTree(_merging_nodes, _incoming_node):
    if len(_merging_nodes) == 1:  # reached end
        merging_node = _merging_nodes.pop(0)
        return createNewNode(merging_node, _incoming_node)

    merging_node = _merging_nodes.pop(0)
    n = createNewNode(merging_node, _incoming_node)
    return buildTree(_merging_nodes, n)


def leftChildren(_count, _node):
    if _node.children[0] is None:
        return 1
    return leftChildren(_count, _node.children[0]) + 1


def rightChildren(_count, _node):
    if _node.children[1] is None:
        return 1
    return rightChildren(_count, _node.children[1]) + 1


def isBalanced(_node):
    number_left = leftChildren(0, _node)
    number_right = rightChildren(0, _node)

    # print("left", number_left)
    # print("right", number_right)

    if number_left == number_right:
        return True
    return False


def findBalanced(_node):
    if _node is None:
        return []
    balanced_node = _node
    merge_list = []
    while not isBalanced(balanced_node):
        # print("Not Balanced!", balanced_node)
        # print("length of list:", len(merge_list))
        # print("1:", balanced_node.children[0])
        # print("2:", balanced_node.children[1])
        # print("3", balanced_node.parent)
        merge_list.insert(0, balanced_node.children[0])
        balanced_node = _node.children[1]
        if balanced_node == _node.children[1]:
            # print("DIAGNOSIS: WARNING")
            break
    # print("Found balanced:", balanced_node)
    merge_list.insert(0, balanced_node)
    return merge_list


def tree_size(root, count=0):
    if root is None:
        return count

    return tree_size(root.children[0], tree_size(root.children[1], count + 1))


class MerkleTree:
    def __init__(self, _node):
        self.root = _node
        self.leaf_nodes = [_node]

        # intialise itself as left child and parent
        _node.setChild(0, _node)
        _node.setParent(_node)

    def add(self, _node):
        # Add hashed entries to tree
        self.leaf_nodes.append(_node)
        self.build()

    # build can only be carried out after the Merkle tree has 2 or more elements
    def build(self):
        leaf_size = len(self.leaf_nodes)
        last_node = self.leaf_nodes[leaf_size - 2]
        incoming_node = self.leaf_nodes[leaf_size - 1]

        if leaf_size == 2:  # handle 1 only
            last_node.children[0] = None
            self.root = buildTree([last_node], incoming_node)
        else:
            # root should never be none
            merge_list = findBalanced(self.root)
            # print("merge_list", merge_list)
            self.root = buildTree(merge_list, incoming_node)

    def get_proof(self, _node):
        # Get membership proof for entry
        proof = []
        current_node = _node
        while current_node.hasParent():
            partner = current_node.findPartner()
            if partner is None:
                # Sound warning, this should not happen
                print("WARNING: ERROR ENCOUNTERED AT {}".format(current_node.data))
            proof.append(current_node.findPartner())
            current_node = current_node.parent
        return proof

    def get_root(self):
        # Return the current root
        return self.root

    def set_root(self):
        current_node = self.leaf_nodes[0]
        while current_node.parent is not None:
            current_node = current_node.parent
        self.root = current_node

    def count_elements(self):
        return tree_size(self.root)


def verify_proof(entry, proof, root):
    # Verifies proof for entry and given root. Returns boolean.
    # Entry must be a node
    # proof must be a list of Nodes
    # root to be compared (if entry + proof == root, return True)
    for nodes in proof:
        entry = MerkleNode("", hashItem(entry.data["Transaction"] + nodes.data["Transaction"]))
    if entry.data["Transaction"] == root.data["Transaction"]:
        return True
    return False


if __name__=='__main__':

    randomDict = {}
    sender = generateRandomString(12)
    randomDict[sender] = 1

    n = MerkleNode("Leaf", json.dumps({"Sender": sender}))
    m = MerkleTree(n)

    for i in range(300):
        while sender in randomDict:
            sender = generateRandomString(12)
        randomDict[sender] = 1
        n1 = MerkleNode("Leaf", json.dumps({"Sender": sender}))
        m.add(n1)

    print("-------------- REPORT ------------------")

    print("size of tree:", m.count_elements())
    print("total transactions:", len(m.leaf_nodes))

    # this should be true
    print("valid verification:", verify_proof(n, m.get_proof(n), m.root))

    # this should be false
    print("invalid verification:", verify_proof(n, m.get_proof(n) + [MerkleNode("", json.dumps({"Sender": "attacker"}))], m.root))

    print("------------ REPORT END ----------------")
