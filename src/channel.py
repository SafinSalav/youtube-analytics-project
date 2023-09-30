import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YouTube_API')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.title = self.get_info()['items'][0]['snippet']['title']
        self.description = self.get_info()['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = self.get_info()['items'][0]['statistics']['subscriberCount']
        self.video_count = self.get_info()['items'][0]['statistics']['videoCount']
        self.view_count = self.get_info()['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self._channel_id

    def get_info(self):
        """Возвращает информацию о канале."""
        channel = self.get_service().channels().list(id=self._channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = self.get_service().channels().list(id=self._channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return youtube

    def to_json(self, name):
        data = {'id': self.channel_id, 'title': self.title, 'description': self.description, 'url': self.url, 'subscriber count': self.subscriber_count, 'video count': self.video_count, 'view count': self.view_count}
        with open(name, 'w') as file:
            json.dump(data, file)

