import requests
import config


user_id = "7812543"
request_url = config.get_request_url() + user_id
headers = config.get_headers()
payload = { "email":"ella@bella.com" }


response = requests.put(url=request_url, headers=headers, data=payload)
print(response.json())