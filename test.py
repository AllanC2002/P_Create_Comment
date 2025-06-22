import requests

login_data = {
    "User_mail": "ascorread1",
    "password": "1234"
}
login_response = requests.post("http://localhost:8080/login", json=login_data)

if login_response.status_code != 200:
    print("Error al iniciar sesión:", login_response.status_code, login_response.text)
    exit()

token = login_response.json()["token"]
print("Token:", token)

comment_data = {
    "Id_publication": "68576f513ac5b69dd669e328",
    "Comment": "Test comment by the developer"
}

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.post("http://localhost:8081/create-comment", json=comment_data, headers=headers)

print("Status:", response.status_code)
print("Response:", response.json())
