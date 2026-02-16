import pytest
from src.channel import Channel


@pytest.fixture
def moscowpython():
    return Channel("UC-OVMPlMA3-YCIeg4z5z23A")


@pytest.fixture
def highload():
    return Channel('UCwHL6WHUarjGfUM_586me8w')


def test_str(moscowpython):
    assert str(moscowpython) == (
        'MoscowPython '
        '(https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    )


def test_magical_methods(moscowpython, highload):
    assert moscowpython + highload == 115800
    assert moscowpython - highload == -59600
    assert highload - moscowpython == 59600
    assert not moscowpython > highload
    assert not moscowpython >= highload
    assert moscowpython < highload
    assert moscowpython <= highload
    assert not moscowpython == highload
