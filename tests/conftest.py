import pytest
from brownie import config
from brownie import Contract


@pytest.fixture
def example_fixture():
    yield "I'm a Fixture"