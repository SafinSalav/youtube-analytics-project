import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YouTube_API')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, id_video):
        self.id_video = id_video
        self.url = f'https://youtu.be/{self.id_video}'
        try:
            self.title = self.video_response()['items'][0]['snippet']['title']
            self.view_count = self.video_response()['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response()['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.view_count = None
            self.like_count = None

    def video_response(self):
        return youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',id=self.id_video).execute()

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist

