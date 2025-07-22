import requests
import config


request_url = config.get_request_url()


def get_by_id(user_id: int | None) -> list[dict[str, str]]:
    id = str(user_id) if isinstance(int(user_id), int) else ""
    return get_handler(id)


def get_handler(id: str) -> list[dict[str, str]]:
    MAX_ATTEMPTS = 3
    TIMEOUT = 1.2
    data = []
    for i in range(1, MAX_ATTEMPTS + 1):
        try:
            response = requests.get(url=request_url + id, timeout=TIMEOUT)
            response.raise_for_status()  # Ensure we catch HTTP errors.
            data = response.json()
            break
        except (requests.exceptions.HTTPError, 
                requests.exceptions.Timeout, 
                requests.exceptions.RequestException, 
                ValueError) as e:
            print(f"Attempt {i} failed: {e}")
    return data if data else [{"all_attempts": "failed"}]


print(f"Get method: {get_by_id(7814305)}")