from src.channel import Channel
import pytest


@pytest.fixture
def channel1():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    return moscowpython


@pytest.fixture
def channel2():
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')
    return highload


def test_str(channel1):
    assert str(channel1) == 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'


def test_math(channel1, channel2):
    assert channel1 + channel2 == 103800
    assert channel1 - channel2 == -50800
    assert channel2 - channel1 == 50800
    assert (channel1 > channel2) is False
    assert (channel1 >= channel2) is False
    assert (channel1 < channel2) is True
    assert (channel1 <= channel2) is True
    assert (channel1 == channel2) is False
