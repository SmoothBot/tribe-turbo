import pytest
from brownie import config
from brownie import Contract


@pytest.fixture
def owner(accounts):
    yield accounts[0]


@pytest.fixture
def auth(accounts):
    yield accounts[1]


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
def turbo_pool(fuse_pool_directory, fuse_comptroller, fuse_oracle, owner):
    close_factor = int(0.50 * 1e18) # 50%
    liquidation_incentive = int(1 * 1e18) # 1%
    pool = fuse_pool_directory.deployPool(
        'Turbo Master Pool', 
        fuse_comptroller, 
        True, 
        close_factor,
        liquidation_incentive,
        fuse_oracle,
        {'from': owner}
    )
    yield pool.events['PoolRegistered']['pool'][2]


@pytest.fixture
def turbo_master(TurboMaster, turbo_pool, fei, owner, auth):
    yield TurboMaster.deploy(turbo_pool, fei, owner, auth, {'from': owner})