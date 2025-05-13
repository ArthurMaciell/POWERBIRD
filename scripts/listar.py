import requests
import pandas as pd
from datetime import datetime, timezone


page = 1
start_date = '2025-01-01'
end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

df_total = pd.DataFrame()




headers = {"accept": "application/json"}

while True:
    url = (
    f"https://crm.rdstation.com/api/v1/deals?page={page}"
    f"&limit=200&created_at_period=true&start_date={start_date}"
    f"T08%3A00%3A00&end_date={end_date}"
    f"T18%3A00%3A00&token=681a40c4468df10014d4bf51")
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Erro na página {page}: {response.status_code}")
        print(response.text)
        break
    
    dados = response.json()
    negociacoes = dados.get("deals", [])
    
    if not negociacoes:
        print("🚫 Nenhuma negociação nova. Fim da paginação.")
        break

    # Transforma em DataFrame e concatena
    df_pagina = pd.json_normalize(negociacoes)
    df_total = pd.concat([df_total, df_pagina], ignore_index=True)

    print(f"✅ Página {page} adicionada: {len(df_pagina)} registros")
    page += 1

# === Resultado final ===
print(f"\n📊 Total de negociações carregadas: {len(df_total)}")

# (opcional) Salvar para CSV ou banco SQLite
caminho = r"C:\Users\Orçamento\OneDrive - GRUPO RETEC\02. Engenharia\Dep. Orçamentos\POWERBI\AUTOMACAO RD\data\negociacoes_2025.xlsx"
df_total.to_excel(caminho, index=False)


