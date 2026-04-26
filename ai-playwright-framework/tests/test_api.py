import json

def test_login_api(playwright):
    request = playwright.request.new_context()

    response = request.post(
        "https://dummyjson.com/auth/login",  # Path lagana zaroori hai
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "username": "emilys",
            "password": "emilyspass",
        })
    )

    print(f"\nResponse Status: {response.status}")
    assert response.status == 200
    print("Login Successful!")
