import pytest

def test_create_safe(turbo_pool, turbo_master, fei, owner, auth, uni):
    print('hello! turbo_master is a deployed TurboMaster')
    safe = turbo_master.createSafe(uni, {'from': owner})
    # assert False # so we can hit the interactive terminal
