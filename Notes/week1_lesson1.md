Main point is about cryptography

Important slides:
    - slide 9:
        - Crypto hash functions
        - {0,1}* denotes set of all binary 
        - {0,1}^n denotes the set of binary within n
        - therefore, the hash function is about reducing a space comprised of a set of all binaries into a small set.
        - output is called the digest, fingerprint, or just hash.
        
    
    - Collision resistance
        - it is hard to find m1=/=m2 such that H(m1) == H(m2)

    - Pre-image resistance (one-way property)
        - Idea is to create a hash that is one way, such that given H and m, x is easy to find, but not the other way around.
        Given x only, it should be difficult or impossible to derive m. [one-way property]
        H(m) == x
        - Given a hash value x, it should be difficult to find any message m such that x = H(m)

    - 2nd pre-image resistance
        - given input m1, difficult to find m2 such that both hash to the same value.
        i.e H(m1) == H(m2)


    - slide 11: Birthday attack classic problem

    - slide 15: non-interactive Proof-of-Work
        - header field introduced to prevent spam

    - slide 16: recap of private and public keys
    
    - slide 17: the properties of security
        - Authentication
        - Non-repudiation
        - Integrity
        - Unforgeability

    - slide 18: Oracle API
        - msg sent to oracle, Sigma sent back.
        - Sigma here thus refers to signature of the message
    
    - slide 21: Hash chains
        - multiple hashing:
        H(H(H(m)))

    - slide 23: Merkle hash trees 
        - behaves similarly to binary trees
        - height of tree is log2(m), where m is the number of messages in the topmost.

    - slide 24: Insertion and combination. 
        - unsure of how data added in batches protects entire tree

    !!- slide 26: Bloom filters ???
        - Bloom filters are designed to give possible false positives, but no false negatives.
        In other words:
        [Possibly in set, Definitely not in set]
        

    




