#consiste de bloques
#bloques consisten de una transaccion que puede ser desde un objeto 
#hasta solo un mensaje
#los bloques estan conectados por hashing


from block import Block
print("BLOQUE GENESIS")
genesis_block = Block("Chancellor on the brink...",["Satoshi sent 1 BTC to Ivan","Satoshi sent 5 BTC to Hal Finney"])
print(genesis_block.block_hash)
print("SEGUNDO BLOQUE")
second_block = Block(genesis_block.block_hash,["Ivan sent 5 BTC to Liz"])
print(second_block.block_hash)
