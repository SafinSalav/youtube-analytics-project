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
        "https://yt3.ggpht.com/ytc/AIdro_nICP5IhVbBsB-KeNqEnRssp"
        "OBWAFU7r54dPI9y41ew-rs=s88-c-k-c0x00ffffff-no-rj"
    )
    assert channel.subscriber_count == "28100"
    assert channel.video_count == "860"
    assert channel.view_count == "2826298"


def test_channel_id(channel):
    with pytest.raises(AttributeError):
        channel.channel_id = 'Новое название'
