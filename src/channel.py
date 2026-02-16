import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """
    Класс для ютуб-канала.
    """
    def __init__(self, channel_id: str) -> None:
        """
        Создание экземпляра класса Channel.

        :param channel_id: id канала.
        :param title: Название канала.
        :param description: Описание канала.
        :param url: Ссылка на канал.
        :param subscriber_count: Количество подписчиков.
        :param video_count: Количество видео.
        :param view_count: Общее количество просмотров.
        """
        self.__channel_id = channel_id
        channel = self.get_info()
        self.title = (
            channel['items'][0]['snippet']['title']
        )
        self.description = (
            channel['items'][0]['snippet']['description']
        )
        self.url = (
            channel['items'][0]['snippet']['thumbnails']['default']['url']
        )
        self.subscriber_count = (
            channel['items'][0]['statistics']['subscriberCount']
        )
        self.video_count = (
            channel['items'][0]['statistics']['videoCount']
        )
        self.view_count = (
            channel['items'][0]['statistics']['viewCount']
        )

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    def get_info(self) -> dict:
        """
        Возвращает информацию о канале.
        """
        youtube = self.get_service()
        channel = youtube.channels().list(
            id=self.__channel_id,
            part='snippet,statistics'
        ).execute()
        return channel

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        channel = self.get_info()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API.
        """
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """
        Сохраняет в файл json значения атрибутов экземпляра класса Channel
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, ensure_ascii=False, indent=2)
