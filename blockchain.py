""" 
class definition for the blockchain class
Author: Matthew Henschke
"""

#importing block module
from block import Block

# class definition
class Blockchain:
    
    def __init__(self):
        """
        Constructor
        """ 
        self._chain = [] # the list of all blocks
        self.genesis_block() # first block in the chain
    

    def genesis_block(self):
        """
        Method that creates the first block of the chain, known as genesis block
        """
        new_block = Block([], 0)
        self._chain.append(new_block)

    def add_block(self, transactions):
        """
        Method that adds a block to the chain
        param transactions : list of transactions
        """
        prev_hash = self._chain[len(self._chain) - 1]._hash
        new_block = Block(transactions, prev_hash)
        proof = self.proof_of_work(new_block)
        self._chain.append(new_block)
        return proof, new_block
    
    def validate_chain(self):
        """
        Method that validates the chain by checking that all the current and prev hash values are correct
        for each block
        """
        for i in range(1, len(self._chain)):
            if self._chain[i - 1]._hash != self._chain[i-1].generate_hash():
                return False
            if self._chain[i]._hash != self._chain[i].generate_hash():
                return False
            if self._chain[i - 1]._hash != self._chain[i]._prev_hash:
                return False
        return True

    def proof_of_work(self, block, difficulty = 2):
        """
        Method that implements the proof of work of Blockchain
        param block : the block that is being used for the proof of work
        param difficulty : the number of leading zeroes required in the sha256 hexstring output is 2 by default
        """
        proof = block.generate_hash()
        while proof[:difficulty] != '0' * difficulty:
            block._nonce += 1
            proof = block.generate_hash()
        block._nonce = 0
        return proof


    def print_blocks(self):
        """
        Method that prints out the contents of all of the
        blocks in the chain
        """
        for i in range(len(self._chain)):
            current_block = self._chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_info()



