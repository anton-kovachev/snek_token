import pytest
from script.deploy import deploy_snek_token
from moccasin.boa_tools import VyperContract


@pytest.fixture
def snek_token() -> VyperContract:
    return deploy_snek_token()
