from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

URL_BACK = os.getenv('URL_BACK')


class RequestsBack():
    def __init__(self) -> None:
        self.token = ''
        self.url_login = URL_BACK + '/v1/authentication/login'
        self.url_register = URL_BACK + '/v1/authentication/register'
        self.url_createVideo = URL_BACK + '/v1/video/createVideo'
        self.url_allVideos = URL_BACK + '/v1/video/allVideos'

    def Login(self, user, password):
        myobj = {'user': user, 'password': password}
        response = requests.post(self.url_login, json=myobj)
        if response.status_code == 201:
            self.token = response.json()['accessToken']
            return True
        else:
            return False

    def Register(self, user, password):
        myobj = {'user': user, 'password': password}
        response = requests.post(self.url_register, json=myobj)
        if response.status_code == 201:
            return True
        else:
            return False

    def CreateVideo(self, title, thumbnail_path, video_path, description=''):
        myobj = {'title': title, 'thumbnail': thumbnail_path,
                 'description': description}

        format_video = video_path.split("/")[-1].split('.')
        format_image = thumbnail_path.split("/")[-1].split('.')
        arquivo = {
            'video': (video_path.split('/')[-1], open(video_path, 'rb'), f'video/{format_video}'),
            'thumbnail': (thumbnail_path.split('/')[-1], open(thumbnail_path, 'rb'), f'image/{format_image}'),
            'body': json.dumps(myobj)
        }

        response = requests.post(self.url_createVideo,  files=arquivo, headers={
                                 'Authorization': f'Bearer {self.token}'})

        if response.status_code == 201:
            return True
        else:
            return {}

    def AllVideos(self):
        response = requests.get(self.url_allVideos, headers={
            'Authorization': f'Bearer {self.token}'})

        if response.status_code == 200:
            return response.json()
        else:
            return {}
