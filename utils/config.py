from dotenv import load_dotenv
import os
from logger import  Logger
load_dotenv()



class Config:

    def __init__(self):

       self.username = os.getenv("USERNAME")
       self.password = os.getenv("PASSWORD")
       self.host =  os.getenv("API_HOST")


config = Config()