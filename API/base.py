
import requests


def test_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = requests.put(url, json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Updated Title"
    print("Post updated successfully:", data)
    print(payload)