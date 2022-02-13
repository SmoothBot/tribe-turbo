import pytest
from brownie import Contract

# def test_create_safe(turbo_pool, turbo_master, fei, owner, auth, uni):
#     print(f'hello! turbo_master is a deployed TurboMaster deployed to {turbo_master.address}')
#     print(f'length of safes... {len(turbo_master.getAllSafes())}')
#     print(f'hello! turbo_masters owner {turbo_master.owner()}')

#     safe = turbo_master.createSafe(uni, {'from': owner})
#     print(f'safe deployed {safe}!')
#     assert False # so we can hit the interactive terminal

# def test_create_safe_without_master(TurboSafe, turbo_master, fei, owner, auth, uni):
#     safe = TurboSafe.deploy(owner, auth, uni, {'from': turbo_master})
#     print(f'safe deployed {safe}')

def test_nefarious_boost(TurboSafe, turbo_master, booster, nefarious_vault, owner, attacker, fei, uni, accounts):
    safe_address, _ = turbo_master.createSafe(uni, {'from': owner}).return_value
    safe = Contract.from_abi("TurboSafe", safe_address, TurboSafe.abi)
    get_fei(fei, safe, accounts)
    booster.setBoostCapForVault(nefarious_vault, 1_000_000)
    booster.setFreezeStatus(False)
    booster.setBoostCapForCollateral(uni, 1_000_000)
    safe.boost(nefarious_vault, 100, {'from': owner})
    assert fei.balanceOf(nefarious_vault) == 100

    safe.less(nefarious_vault, 100, {'from': owner})
    assert fei.balanceOf(nefarious_vault) == 100    


def get_fei(fei, safe, accounts):
    amount = 10_000 * 10 ** fei.decimals()
    # In order to get some funds for the token you are about to use,
    # it impersonate the uniswap LP pool
    reserve = accounts.at("0x956F47F50A910163D8BF957Cf5846D573E7f87CA", force=True)
    fei.transfer(safe, amount, {"from": reserve})