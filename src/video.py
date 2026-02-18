import json
from src.channel import Channel


class Video:
    """
    Класс для видео.
    """
    def __init__(self, video_id: str) -> None:
        """
        Инициализация экземпляра Video.

        :param video_id: id видео.
        :param title: Название видео.
        :param url: Ссылка на видео.
        :param view_count: Количество просмотров.
        :param like_count: Количество лайков.
        """
        self.video_id: str = video_id
        video_response: dict = self.get_info()
        self.title: str = (
            video_response['items'][0]['snippet']['title']
        )
        self.url: str = (
            f'https://youtu.be/{self.video_id}'
        )
        self.view_count: int = int(
            video_response['items'][0]['statistics']['viewCount']
        )
        self.like_count: int = int(
            video_response['items'][0]['statistics']['likeCount']
        )

    def get_info(self) -> dict:
        """
        Получает информацию о видео.
        """
        youtube = Channel.get_service()
        return youtube.videos().list(
            part='snippet,statistics,contentDetails,topicDetails',
            id=self.video_id
        ).execute()

    def print_info(self) -> None:
        """
        Выводит информацию о видео.
        """
        print(json.dumps(self.get_info(), indent=2, ensure_ascii=False))

    def __str__(self) -> str:
        """
        Возвращает название видео.
        """
        return self.title


class PLVideo(Video):
    """
    Класс для видео из плейлиста.
    """
    def __init__(self, video_id, playlist_id) -> None:
        """
        Инициализирует экземпляр PLVideo из родительского класса Video

        :param playlist_id: id плейлиста.
        """
        super().__init__(video_id=video_id)
        self.playlist_id = playlist_id
