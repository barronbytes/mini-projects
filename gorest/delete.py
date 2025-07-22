import requests
import config


user_id = "7812543"
request_url = config.get_request_url() + user_id
headers = config.get_headers()


response = requests.delete(url=request_url, headers=headers)
print(response)