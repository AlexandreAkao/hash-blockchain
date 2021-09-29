from block import Block

class Blockchain:
  def __init__(self):
    self.blocks = []
    self.generate_genesis()
  
  def generate_genesis(self):
    genesis = Block(0, "genesis block", 0)
    hash = genesis.encrypt()
    print(f'[ {genesis.nonce} ]')
    self.blocks.append(hash)

  def add_new_block(self, transactions):
    index = len(self.blocks)
    previous_hash = self.blocks[-1]
    new_block = Block(index, transactions, previous_hash)
    hash = new_block.encrypt()
    print(f'[ {new_block.nonce} ]')
    self.blocks.append(hash)

  def blockchain_is_valid(self):
    invalid_blocks = list(filter(lambda hash: not hash.startswith("000"), self.blocks))
    return True if len(invalid_blocks) == 0 else False