import requests
from utils.config import config
from utils.logger import Logger

logger = Logger().get_logger("automation")

class coreApi:
    def __init__(self):
        self.username = config.username
        self.password = config.password
        self.url = config.host
        self.token = None

    def authToken(self):
        """
         Generate or refresh auth token.
        """
        payload = {"useranme": self.username , "password": self.password}
        try:
            response = requests.post(f"{self.url}/auth", json=payload)
            response.raise_for_status()
            self.token =  response.json()
            return self.token
        except Exception as e :
            logger.error(f"URL {self.url} failed as {e}")
            return None


    def get(self,endpoint):
        if not self.token:
            self.authToken()
        authorization_bearer = {"auth_token" : self.token}
        





