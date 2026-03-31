from contracts import snek_token
from eth_utils import to_wei
from moccasin.boa_tools import VyperContract


INITIAL_SUPPLY = to_wei(1000, "ether")


def deploy_snek_token() -> VyperContract:
    snek_token_contract: VyperContract = snek_token.deploy(INITIAL_SUPPLY)
    print(f"Deployed SnekToken at address: {snek_token_contract.address}")
    return snek_token_contract


def moccasin_main() -> VyperContract:
    return deploy_snek_token()
