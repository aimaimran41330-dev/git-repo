from utils import make_target

def test_happy():
    assert make_target(5) == 1
    assert make_target(4) == 1

def test_unhappy():
    assert make_target(3) == 0
    assert make_target(1) == 0
