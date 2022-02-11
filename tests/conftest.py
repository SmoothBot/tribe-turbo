import pytest
from brownie import Contract


@pytest.fixture
def owner(accounts):
    yield accounts[0]


@pytest.fixture
def auth(MockAuthority, owner):
    yield MockAuthority.deploy(owner, {'from': owner})


# Rari contract addresses: https://docs.rari.capital/contracts/#rari-governance
@pytest.fixture
def fuse_oracle():
    yield Contract('0x1887118E49e0F4A78Bd71B792a49dE03504A764D') # master price oracle


@pytest.fixture
def fuse_comptroller():
    yield Contract('0xE16DB319d9dA7Ce40b666DD2E365a4b8B3C18217')


@pytest.fixture
def fuse_pool_directory():
    yield Contract('0x835482FE0532f169024d5E9410199369aAD5C77E')


@pytest.fixture
def fei(interface):
    yield interface.ERC20('0x956F47F50A910163D8BF957Cf5846D573E7f87CA')

@pytest.fixture
def fei(interface):
    yield interface.ERC20('0x956F47F50A910163D8BF957Cf5846D573E7f87CA')

@pytest.fixture
def uni(interface):
    yield interface.ERC20('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')

@pytest.fixture
def turbo_pool(fuse_pool_directory, fuse_comptroller, fuse_oracle, owner):
    close_factor = int(0.50 * 1e18) # 50%
    liquidation_incentive = int(1 * 1e18) # 1%
    tx = fuse_pool_directory.deployPool(
        'Turbo Master Pool', 
        fuse_comptroller, 
        True, 
        close_factor,
        liquidation_incentive,
        fuse_oracle,
        {'from': owner}
    )
    addr = (tx.events['PoolRegistered']['pool'][2])
    pool = Contract.from_abi("Comptroller", addr, fuse_comptroller.abi)

    # TODO - Deploy CToken for fei and add market to our new fuse pool!??

    yield pool

@pytest.fixture
def turbo_master(TurboMaster, MockComptroller, fei, owner, auth):
    mock_comptroller = MockComptroller.deploy({'from': owner})
    turboMaster = TurboMaster.deploy(mock_comptroller, fei, owner, auth, {'from': owner})
    turboMaster.setDefaultSafeAuthority(auth)
    yield turboMaster