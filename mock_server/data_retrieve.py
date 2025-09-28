import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data.json")

def get_users():
    try:
        with  open(file_path,"r") as f:
            return json.load(f)

    except Exception as e:
        raise e


def add_user(user):
        users = get_users()
        users.append(user)
        with  open(file_path,"w") as f:
            json.dump(user,f)
