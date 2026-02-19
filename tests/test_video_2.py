import pytest
from src.video import Video


@pytest.fixture
def broken_video():
    return Video('broken_video_id')


def test_video_init(broken_video):
    assert broken_video.title is None
    assert broken_video.like_count is None
