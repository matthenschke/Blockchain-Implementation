"""
test code for blockchain implementation
Author: Matthew Henschke 
"""
# importing modules
from blockchain import Blockchain
from block import Block



if __name__ == "__main__":

    # testing all functionality of the blockchain and block classes
    chain = Blockchain() # creating the blockchain

    # creating transactions
    transactions1 = [{"amount" : "40.00", "sender" : "Alice", "receiver" : "Bob"}] 
    transactions1.append({"amount" : "40.00", "sender": "Mary", "receiver" : "Jack"})
    transactions2 = [{"amount" : "20.20", "sender" : "Alice", "receiver" : "Bob"}] 
    transactions2.append({"amount" : "50.00", "sender": "Mary", "receiver" : "Matt"})

    # adding the transactions to the blockchain
    print(chain.add_block(transactions1))
    print(chain.add_block(transactions2))

    # printing out all blocks
    chain.print_blocks()
    