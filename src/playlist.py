import os
import datetime
import json
import isodate

from googleapiclient.discovery import build

api_key: str = os.getenv('YouTube_API')
youtube = build('youtube', 'v3', developerKey=api_key)


class PlayList:
    __slots__ = ('id_playlist', 'title', 'url')

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        self.title = self.title_playlist()
        self.url = f'https://www.youtube.com/playlist?list={self.id_playlist}'

    def playlist_response(self):
        return youtube.playlistItems().list(playlistId=self.id_playlist, part='snippet', maxResults=50).execute()

    def title_playlist(self):
        channel_id = self.playlist_response()['items'][0]['snippet']['channelId']
        playlists = youtube.playlists().list(channelId=channel_id, part='contentDetails,snippet', maxResults=50).execute()
        for i in playlists['items']:
            if i['id'] == self.id_playlist:
                return i['snippet']['title']

    def id_videos_of_playlist(self):
        id_videos = []
        for i in self.playlist_response()['items']:
            id_videos.append(i['snippet']['resourceId']['videoId'])
        return id_videos

    def video_response(self, id_video):
        return youtube.videos().list(part='statistics,contentDetails',id=id_video).execute()

    @property
    def total_duration(self):
        sum_duration = datetime.timedelta(0)
        for i in self.id_videos_of_playlist():
            duration = isodate.parse_duration(self.video_response(i)['items'][0]['contentDetails']['duration'])
            sum_duration += duration
        return sum_duration

    def show_best_video(self):
        list_of_likeCount = []
        for i in self.id_videos_of_playlist():
            list_of_likeCount.append(int(self.video_response(i)['items'][0]['statistics']['likeCount']))
        list_of_likeCount.sort()
        for i in self.id_videos_of_playlist():
            if int(self.video_response(i)['items'][0]['statistics']['likeCount']) == list_of_likeCount[-1]:
                return f"https://youtu.be/{self.video_response(i)['items'][0]['id']}"




