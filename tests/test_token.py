from conftest import snek_token
from eth_utils import to_wei
from script.deploy import INITIAL_SUPPLY
import boa


RANDOM_USER = boa.env.generate_address("Random User")


def test_token_name(snek_token):
    # Check the name of the token
    assert snek_token.name() == "snek_token"


def test_token_total_supply(snek_token):
    # Check the total supply of the token
    assert snek_token.totalSupply() == INITIAL_SUPPLY  # Assuming 18 decimals


def test_snek_token_emits_a_transfer_event(snek_token):
    with boa.env.prank(snek_token.owner()):
        snek_token.transfer(RANDOM_USER, to_wei(1, "ether"))
        logs = snek_token.get_logs()
        # Access event fields directly as attributes
        assert logs[0].sender == snek_token.owner()
        assert logs[0].receiver == RANDOM_USER
        assert logs[0].value == to_wei(1, "ether")
