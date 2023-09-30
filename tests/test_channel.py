from src.channel import Channel
import pytest


@pytest.fixture()
def channel():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    return moscowpython


def test_attributes(channel):
    assert channel.title == 'MoscowPython'
    assert channel.video_count == '708'
    assert channel.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'


def test_new_id(channel):
    with pytest.raises(AttributeError):
        channel.channel_id = 'Новое название'


def test_get_service(channel):
    assert channel.get_service() is not None


def test_to_json(channel):
    channel.to_json('moscowpython.json')
