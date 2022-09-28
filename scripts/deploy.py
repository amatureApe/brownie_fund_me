from brownie import network, config, FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account, get_verify_status


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract

    # if on persistent network, use associated address
    # otherwise, deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        mock_aggregator = MockV3Aggregator.deploy(
            18,
            2000000000000000000000,
            {"from": account},
            publish_source=get_verify_status(),
        )
        price_feed_address = mock_aggregator.address
        print("Mocks Deployed")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=get_verify_status(),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
