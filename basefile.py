from web3 import Web3

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

# Your Ethereum account private key
private_key = "YOUR_PRIVATE_KEY"

# The address of the MetaMask wallet you want to send Ether to
to_address = "YOUR_METAMASK_WALLET_ADDRESS"

# The address of your Ethereum account
from_address = w3.eth.account.privateKeyToAccount(private_key).address

# Check the balance of your account
balance = w3.eth.getBalance(from_address)
print(f'Balance: {balance} wei')

# Convert the balance to Ether
balance_ether = w3.fromWei(balance, 'ether')
print(f'Balance: {balance_ether} ether')

# The amount of Ether you want to send
amount = 1

# Build the transaction
tx = {
    'to': to_address,
    'from': from_address,
    'value': w3.toWei(amount, 'ether'),
    'gas': 21000,
    'gasPrice': w3.eth.gasPrice,
    'nonce': w3.eth.getTransactionCount(from_address)
}

# Sign the transaction
signed_tx = w3.eth.account.signTransaction(tx, private_key)

# Send the transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

# Wait for the transaction to be mined
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Print the transaction receipt
print(tx_receipt)
