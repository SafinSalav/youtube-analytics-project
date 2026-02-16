import pytest
from src.channel import Channel


@pytest.fixture
def channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_init(channel):
    assert channel.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'
