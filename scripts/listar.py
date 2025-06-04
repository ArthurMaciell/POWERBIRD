import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import pandas as pd
from datetime import datetime, timezone
from utils.auth import get_rdstation_token
from scripts.ajuste_dist import ajustar_dist
from scripts.ajuste_rep import ajustar_rep

page = 1
start_date = '2025-01-01'
#end_date = '2024-12-31'
end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
df_total = pd.DataFrame()

token = get_rdstation_token()
headers = {"accept": "application/json"}

while True:
    url = (
        f"https://crm.rdstation.com/api/v1/deals?page={page}"
        f"&limit=200&created_at_period=true&start_date={start_date}"
        f"T08%3A00%3A00&end_date={end_date}"
        f"T18%3A00%3A00&token={token}"
    )

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

    df_pagina = pd.json_normalize(negociacoes)
    df_total = pd.concat([df_total, df_pagina], ignore_index=True)

    print(f"✅ Página {page} adicionada: {len(df_pagina)} registros")
    page += 1



# 2) Garanta que a coluna seja lista de dicts
def parse_custom_fields(s):
    if isinstance(s, str):
        try:
            return ast.literal_eval(s)
        except (ValueError, SyntaxError):
            return []
    elif isinstance(s, list):
        return s
    else:
        return []
df_total.loc[:, "deal_custom_fields"] = df_total["deal_custom_fields"].apply(parse_custom_fields)

# 3) Função que retorna um dict {label: value} para cada linha
def expandir_campos(campos):
    resultado = {}
    for campo in campos:
        cf = campo.get("custom_field", {})
        label = cf.get("label")
        if label:
            resultado[label] = campo.get("value")
    return resultado

# 4) Aplique a expansão e transforme em DataFrame
df_custom = df_total["deal_custom_fields"] \
    .apply(expandir_campos) \
    .apply(pd.Series)

# 5) Una ao DataFrame original
df_expanded = pd.concat([df_total, df_custom], axis=1)

# Agora cada label virou uma coluna, ex:
#print(df_expanded.columns)       # verá colunas como 'Fator', 'Proposta Nº', 'Unidade de Negócio', …
#print(df_expanded[["id", "user.name", "Fator", "Proposta Nº", "Unidade de Negócio"]].head())



# Salvar
caminho = r"C:\\Users\\Orçamento\\OneDrive - GRUPO RETEC\\02. Engenharia\\Dep. Orçamentos\\POWERBI\\AUTOMACAO RD\\data\\negociacoes_2025.xlsx"
df_expanded.to_excel(caminho, index=False)

# Garante que a pasta de logs exista
log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)

log_path = os.path.join(log_dir, "execucao.log")

with open(log_path, "a", encoding="utf-8") as f:
    f.write(f"Executado com sucesso em {datetime.now()}\n")
    

ajustar_dist(caminho)
ajustar_rep(caminho)

print('Deu certo!!!')