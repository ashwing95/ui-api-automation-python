import requests
from dotenv import load_dotenv
import os
load_dotenv()


class ApiHelper:

    def __init__(self):
        self.url = os.getenv("API_URL")

    def get_name(self):
        user_list = []
        response = requests.get(f" {self.url}/get_users")
        data = response.json()
        for obj in data:
            user_list.append(obj["name"])
        return user_list







