import pytest

# def test_create_safe(turbo_pool, turbo_master, fei, owner, auth, uni):
#     print(f'hello! turbo_master is a deployed TurboMaster deployed to {turbo_master.address}')
#     print(f'length of safes... {len(turbo_master.getAllSafes())}')
#     print(f'hello! turbo_masters owner {turbo_master.owner()}')

#     safe = turbo_master.createSafe(uni, {'from': owner})
#     print(f'safe deployed {safe}!')
    # assert False # so we can hit the interactive terminal

def test_create_safe_without_master(TurboSafe, nefarious_turbo_master, fei, owner, auth, uni):
    safe = TurboSafe.deploy(owner, auth, uni, {'from': nefarious_turbo_master})
    print(f'safe deployed {safe}')
