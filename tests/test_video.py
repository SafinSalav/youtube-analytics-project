from src.video import Video, PLVideo
import pytest


@pytest.fixture
def video1():
    return Video('AWX4JnAnjBE')


@pytest.fixture
def video2():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_video1(video1):
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_video2(video2):
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

