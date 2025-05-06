import requests

url = "https://api.rd.services/auth/token?token_by=refresh_token"

payload = {
    "client_id": "c601b04b-76d5-486f-a0d6-644c8b19b069",
    "client_secret": "cee29c91bca5478c81ae54f56a464312",
    "refresh_token": "iePyN3gAHpPtWIU4ynXZzh_lOQ5O5mbRNMopeZIfKs0"
}

headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    tokens = response.json()
    print("✅ Novo access_token:", tokens["access_token"])
    print("🔁 Novo refresh_token:", tokens["refresh_token"])
else:
    print("❌ Erro ao renovar token:", response.status_code)
    print(response.text)
