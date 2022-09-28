from brownie import MockV3Aggregator, network, config, accounts

FORKED_LOCAL_ENVIRONMETNS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active in FORKED_LOCAL_ENVIRONMETNS
    ):
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
            STARTING_PRICE,
            {"from": get_account()},
            publish_source=get_verify_status(),
        )
    print("Mocks Deployed")
