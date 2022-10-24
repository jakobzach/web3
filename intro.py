## https://ethereum.org/en/developers/tutorials/a-developers-guide-to-ethereum-part-one/

from web3 import Web3

#print(Web3.toWei(1, 'ether'))

w3 = Web3(Web3.EthereumTesterProvider())
print(w3.isConnected())

# print(w3.eth.accounts)

# for acc in w3.eth.accounts:
#     print(w3.fromWei(w3.eth.get_balance(acc), 'ether'))

print(w3.eth.get_block('latest'))
