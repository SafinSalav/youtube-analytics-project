from src.video import Video, PLVideo
import pytest


@pytest.fixture
def video1():
    return Video('AWX4JnAnjBE')


@pytest.fixture
def video2():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_Video_init(video1):
    assert video1.video_id == "AWX4JnAnjBE"
    assert video1.title == "GIL в Python: зачем он нужен и как с этим жить"
    assert video1.url == "https://youtu.be/AWX4JnAnjBE"
    assert video1.view_count == 66059
    assert video1.like_count == 2712


def test_PLVideo_init(video2):
    assert video2.video_id == '4fObz_qw9u4'
    assert video2.title == "MoscowPython Meetup 78 - вступление"
    assert video2.url == "https://youtu.be/4fObz_qw9u4"
    assert video2.view_count == 763
    assert video2.like_count == 10
    assert video2.playlist_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'


def test_str(video1, video2):
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'
