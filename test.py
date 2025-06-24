import requests

login_data = {
    "User_mail": "allan",
    "password": "1234"
}
login_response = requests.post("http://52.203.72.116:8080/login", json=login_data)

if login_response.status_code != 200:
    print("Error al iniciar sesión:", login_response.status_code, login_response.text)
    exit()

token = login_response.json()["token"]
print("Token:", token)

comment_data = {
    "Id_publication": "6858bb431ed97d52a0c6c02f",
    "Comment": "Test comment by the developer"
}

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.post("http://3.221.235.171:8080/create-comment", json=comment_data, headers=headers)

print("Status:", response.status_code)
print("Response:", response.json())
