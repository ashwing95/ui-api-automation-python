import requests
from operator import itemgetter
from jsonschema  import validate

def fetch_users():

    try:
        response = requests.get("http://127.0.0.1:5000/get_users" , timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Exception raised {e}")
        return

    assert response.status_code == 200 , f" Expected code 200 , got response {response.status_code} "


    data = response.json()

    validate(instance = data , schema= schema_validate())

    get_name = itemgetter('name')

    namelist = list(map(get_name,data))

def schema_validate():
    schema = {
        "type" : "array",
        "items": {
            "type" : "object" ,
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "email": {"type": "string"}

        } ,
            "required": ["id", "name", "email"]

        }
    }

    return schema



if __name__ == "__main__":
    fetch_users()