import pandas as pd


def ajustar_dist(caminho):
    df = pd.read_excel(caminho)
    
    colunas = [
        "id", "name",'Proposta Nº','organization.name','Nome da Obra','Unidade de Negócio','Fator','Local da Obra (Estado)',
        'Local da Obra (Cidade)','Produtos (Representação)',
        'Fábrica (Representação)','Orçamentista', "amount_total", "amount_unique", "markup",
        "created_at", "closed_at", "last_activity_at",
        "interactions", "win", "deal_stage.name", "user.id", "user.name",
        "deal_lost_reason.name","Tipo de Contato", "Fonte de Contato" , "Tipo de Obra", "Produtos (Distribuição)"  
    ]
    
    df_dist = df[df['user.name'].isin(['Luan Araújo', 'Iago Rangel','Wellisson Chaves','Rutemar Júnior','Marlon Souza'])]
    df_dist = df_dist[colunas].copy()
    df_dist.loc[:, "Fator"] = (
        df_dist["Fator"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float, errors="ignore")
    )
    total_orc = len(df_dist["deal_stage.name"] == "Venda Ganha") + len(df_dist["deal_stage.name"] == "Venda Perdida") + len(df_dist["deal_stage.name"] == "Venda Cancelada")
    taxa_conversão_rep = df_dist[df_dist["deal_stage.name"] == "Venda Ganha"].shape[0]/total_orc
    df_dist['Fator'] = pd.to_numeric(df_dist['Fator'], errors='coerce')
    df_dist['Fator'] = df_dist['Fator'].astype(float)
    
    estagios_validos = ['Venda Ganha',"Venda Perdida", "Venda Cancelada"]
    df_validos = df_dist[df_dist["deal_stage.name"].isin(estagios_validos)] 
    total = df_validos.groupby("organization.name").size()
    ganhas = df_validos[df_validos['deal_stage.name']== "Venda Ganha"].groupby('organization.name').size()
    taxa_conversao = (ganhas / total)
    df_dist["taxa_conversao"] = df["organization.name"].map(taxa_conversao)
    
    caminho_dist = r"C:\Users\Orçamento\ONE DRIVE ORCAMENTO\OneDrive - GRUPO RETEC\02. Engenharia\Dep. Orçamentos\POWERBI\AUTOMACAO RD\data\negociacoes_dist_2025.xlsx"
    df_dist.to_excel(caminho_dist)