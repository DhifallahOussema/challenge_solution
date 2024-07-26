from web3 import Web3

INFURA_URL = "https://mainnet.infura.io/v3/a6f3ca26f95b4df7af2def15a766a379"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))


def get_eth_balance(address):
    if web3:

        balance_eth = web3.eth.get_balance(address)

        return balance_eth
    else:
        raise ConnectionError("Unable to connect to the Ethereum network")
