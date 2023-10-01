from src.playlist import PlayList
import pytest
import datetime


@pytest.fixture
def pl():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test(pl):
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"


def test_total_duration(pl):
    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0


def test_best_video(pl):
    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
