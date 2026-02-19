from src.channel import Channel
from src.printj import printj
import datetime
import isodate


class PlayList:
    """
    Класс для плейлистов.

    :param youtube: Объект для работы с YouTube API.
    """
    youtube = Channel.get_service()

    def __init__(self, playlist_id: str) -> None:
        """
        Инициализирует экземпляр класса PlayList.

        :param playlist_id: id плейлиста.
        :param title: Название плейлиста.
        :param url: Ссылка на плейлист.
        """
        self.__playlist_id: str = playlist_id
        playlist_info: dict = self.get_playlist_info()
        self.title: str = playlist_info['items'][0]['snippet']['title']
        self.url: str = (
                f'https://www.youtube.com/playlist?list={self.__playlist_id}'
        )

    @property
    def playlist_id(self) -> str:
        """
        Возвращает id плейлиста.
        """
        return self.__playlist_id

    def get_playlist_info(self) -> dict:
        """
        Возвращает информацию о плейлисте.
        """
        return PlayList.youtube.playlists().list(
            id=self.__playlist_id,
            part='snippet'
        ).execute()

    def get_playlist_videos_info(self) -> dict:
        """
        Возвращает информацию о видео в плейлисте.
        """
        return PlayList.youtube.playlistItems().list(
            playlistId=self.__playlist_id,
            part='contentDetails',
            maxResults=50
        ).execute()

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о плейлисте и видео в нем.
        """
        print('Информация о плейлисте:')
        printj(self.get_playlist_info())
        print('\nИнформация о видео в плейлисте:')
        printj(self.get_videos_info())

    def get_video_ids(self) -> list[str]:
        """
        Возвращает список id всех видео в плейлисте.
        """
        return [
            video['contentDetails']['videoId']
            for video in self.get_playlist_videos_info()['items']
        ]

    def get_videos_info(self) -> dict:
        """
        Возвращает информацию о каждом видео из плейлиста.
        """
        return PlayList.youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(self.get_video_ids())
        ).execute()

    def get_videos_duration(self) -> dict:
        """
        Возвращает словарь с длительностью каждого видео.
        """
        videos_duration = {}
        for video in self.get_videos_info()['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            videos_duration[video['id']] = duration
        return videos_duration

    @property
    def total_duration(self) -> datetime.timedelta:
        """
        Возвращает суммарную длительность плейлиста.
        """
        total_duration = datetime.timedelta(0)
        for values in self.get_videos_duration().values():
            total_duration += values
        return total_duration

    def show_best_video(self) -> str:
        """
        Возвращает ссылку на самое популярное видео
        из плейлиста (по количеству лайков).
        """
        videos_like_count = self.get_videos_like_count()
        most_popular_video_id = max(
            videos_like_count,
            key=videos_like_count.get
        )
        return f'https://youtu.be/{most_popular_video_id}'

    def get_videos_like_count(self) -> dict:
        """
        Возвращает словарь с количеством лайков каждого видео.
        """
        videos_like_count = {}
        for video in self.get_videos_info()['items']:
            videos_like_count[video['id']] = int(
                video['statistics']['likeCount']
            )
        return videos_like_count
