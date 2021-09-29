from blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_new_block('Bloco 1')
blockchain.add_new_block('Bloco 2')
blockchain.add_new_block('Bloco 3')


print(blockchain.blockchain_is_valid())

print(blockchain.blocks)