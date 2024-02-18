import requests

params = {
    "name": "test_user_3",
    "password": "1q2w3E4R"
}

response = requests.post(url="http://127.0.0.1:8000/add-user", json=params)
