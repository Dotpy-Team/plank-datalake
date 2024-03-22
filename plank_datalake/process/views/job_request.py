import requests


login_url = 'http://127.0.0.1:8000/api/jobs/'
login_data = {
    "username": "luiz.cairo@dotpy.com.br",
    "password": "123456" 
}

response = requests.post(login_url, json=login_data)

if response.status_code == 200:
    token_data = response.json()
    token_jwt = token_data.get("token")

    print("Token JWT obtido com sucesso:", token_jwt)
else:
    print(f"Erro ao fazer o login: {response.status_code}")


# token_jwt = token_data.get("token")

# url = "http://127.0.0.1:8000/api/jobs/"

# headers = {
#     "Authorization": f"Bearer {token_jwt}",
#     "Content-Type": "application/json" 
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:

#     job_execution_data = response.json()

#     print(job_execution_data)
# else:
#     print(f"Erro: {response.status_code}")
