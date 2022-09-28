from brownie import network, config, FundMe, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=get_verify_status(),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
