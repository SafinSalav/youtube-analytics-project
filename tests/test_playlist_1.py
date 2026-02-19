import datetime
import pytest
from src.playlist import PlayList


@pytest.fixture
def playlist1():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_playlist_init(playlist1):
    assert playlist1.playlist_id == 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'
    assert playlist1.title == "Moscow Python Meetup №81"
    assert playlist1.url == (
        "https://www.youtube.com/playlist?list="
        "PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
    )


def test_get_video_ids(playlist1):
    playlist_videos_info = playlist1.get_playlist_videos_info()
    video_count = playlist_videos_info['pageInfo']['totalResults']
    assert len(playlist1.get_video_ids()) == video_count


def test_total_duration(playlist1):
    duration = playlist1.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0


def test_show_best_video(playlist1):
    assert playlist1.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
