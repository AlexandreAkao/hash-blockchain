from hashlib import sha256
from datetime import datetime

class Block:
  def __init__(self, index, transactions, previous_hash):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    self.index = index
    self.transactions = transactions
    self.timestamp = timestamp
    self.previous_hash = previous_hash
    self.nonce = 1

  def encrypt(self):
    while True:
      hash_block = sha256(self.get_block_string()).hexdigest()
      is_hash_valid = self.is_valid(hash_block)
      if is_hash_valid:
        return hash_block
      else:
        self.nonce += 1
    

  def is_valid(self, hash_block):
    return str(hash_block).startswith("000")

  def get_block_string(self):
    formated_string = f'{self.index}{self.transactions.replace(" ", "")}{self.previous_hash}{self.nonce}'.encode("utf-8")
    return formated_string