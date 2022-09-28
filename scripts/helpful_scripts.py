from brownie import MockV3Aggregator, network, config, accounts
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 18
STARTING_PRICE = 2000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_verify_status():
    return config["networks"][network.show_active()].get("verify")


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            Web3.toWei(STARTING_PRICE, "ether"),
            {"from": get_account()},
            publish_source=get_verify_status(),
        )
    print("Mocks Deployed")
