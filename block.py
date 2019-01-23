""" 
class definition for the block class
Author: Matthew Henschke
"""
from hashlib import sha256
from datetime import datetime

# class definition
class Block:
    def __init__(self, transactions, prev_hash, nonce = 0):
        """
        Constructor
        :param transactions : list of transactions
        :param prev_hash : the hash value of the previous block
        :param nonce : blockchain nonce
        """
        self._timestamp = datetime.now() # timestamp when block was created
        self._transactions = transactions
        self._prev_hash = prev_hash
        self._nonce = nonce
        self._hash = self.generate_hash()

    def generate_hash(self):
        """
        Method that generates the hash for the block using SHA256
        """
        block_contents = str(self._timestamp) + str(self._transactions) + str(self._prev_hash) + str(self._nonce)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()
    
    def print_info(self):
        """
        Method that prints out all contents of a block
        """
        print("Transactions: {}".format(self._transactions))
        print("Previous Hash: {}".format(self._prev_hash))
        print("Nonce: {}".format(self._nonce))
        print("Current Hash: {}".format(self.generate_hash()))

        
