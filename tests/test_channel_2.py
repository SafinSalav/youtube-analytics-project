import pytest
from src.channel import Channel


@pytest.fixture
def channel():
    return Channel("UC-OVMPlMA3-YCIeg4z5z23A")


def test_init(channel):
    assert channel.channel_id == "UC-OVMPlMA3-YCIeg4z5z23A"
    assert channel.title == "MoscowPython"
    assert channel.description == (
        "Видеозаписи со встреч питонистов в Москве и не только. "
        ":)\nЧат в ТГ: https://t.me/moscowpythonconf\n"
    )
    assert channel.url == (
        "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"
    )
    assert channel.subscriber_count == 28100
    assert channel.video_count == 864
    assert channel.view_count == 2826634


def test_channel_id(channel):
    with pytest.raises(AttributeError):
        channel.channel_id = 'Новое название'
