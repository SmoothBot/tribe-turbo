import pytest

def test_template(TurboMaster, TurboSafe, example_fixture):
    assert example_fixture == "I'm a Fixture"
    print("You can put yout w... test's in here")