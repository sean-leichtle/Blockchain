import hashlib
from time import time


class Block(object):

    def __init__(self, name, transactions) -> None:
        self.name = name
        self.transactions = transactions
        self.nonce = 0
        self.previous_hash = None
        self.hash_value = self.hash_block()
        self.mining_time = None

    def hash_block(self) -> str:
        enc = (self.name + self.transactions + str(self.nonce) + str(self.previous_hash)).encode('utf-8')
        m = hashlib.sha256(enc) # der eigentliche Hashingvorgang
        return m.hexdigest()    # hier wird der Hashwert oder "digest" als Hexadezimalzahl zurückgegeben

    def mine(self, work) -> None:
        timer_chs = ['|', '/', '-', '\\']   #### Feedback, dass eine Berechnung laeuft - kann entfernt werden
        t1 = time()
        while self.hash_value[0:work] != '0' * work:    # hier werden Noncewerten auspropiert,
            self.nonce += 1                             # bis einen Hashwert gefunden wurde,
            self.hash_value = self.hash_block()         # der mit -work- * 0en anfängt
            print(f"\r{timer_chs[self.nonce % len(timer_chs)]}", end="", flush=True)    #### Feedback, dass eine Berechnung laeuft - kann entfernt werden
        t2 = time()
        self.mining_time = t2 - t1


class Blockchain(object):

    def __init__(self, work) -> None:
        self.blockchain = []
        self.work = work

    def add_block(self, block) -> None:
        if len(self.blockchain) == 0:
            block.previous_hash = "0" * 64
        else:
            block.previous_hash = self.blockchain[-1].hash_value # ...[-1] -> len(self.blockchain) - 1
        block.mine(self.work)
        self.blockchain.append(block)

    def print_blockchain(self) -> None:
        for block in self.blockchain:
            print("Block:\t\t\t", block.name)
            print("Transactions:\t", block.transactions)
            print("Nonce:\t\t\t", block.nonce)
            print("Previous hash:\t", block.previous_hash)
            print("Hash value:\t\t", block.hash_value)
            print("Mining time:\t", block.mining_time, "seconds")
            print("-" * 81)


# MAIN
bc = Blockchain(2)

b1 = Block("Block 1", "Hans 2BTC an Emma")
bc.add_block(b1)
b2 = Block("Block 2", "Sigrid 5BTC an Peter")
bc.add_block(b2)
b3 = Block("Block 3", "Heike 4BTC an Regine")
bc.add_block(b3)
b4 = Block("Block 4", "Sara 3BTC an Frank")
bc.add_block(b4)
b5 = Block("Block 5", "Emma 11BTC an Frank")
bc.add_block(b5)

bc.print_blockchain()
