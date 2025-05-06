import requests

url = "https://api.rd.services/auth/token?token_by=code"

payload = {
    "client_id": "c601b04b-76d5-486f-a0d6-644c8b19b069",
    "client_secret": "cee29c91bca5478c81ae54f56a464312",
    "code": "ae85d8466f2882457b24a4e0849d66f2"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("✅ Token obtido com sucesso!")
    print(response.json())
else:
    print("❌ Erro ao obter token:", response.status_code)
    print(response.text)
