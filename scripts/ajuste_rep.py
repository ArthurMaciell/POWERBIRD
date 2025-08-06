import pandas as pd


def ajustar_rep(caminho):
    df = pd.read_excel(caminho)
    
    colunas = [
        "id", "name",'Proposta Nº','organization.name','Nome da Obra','Unidade de Negócio','Fator','Local da Obra (Estado)',
        'Local da Obra (Cidade)','Produtos (Representação)',
        'Fábrica (Representação)','Orçamentista', "amount_total", "amount_unique", "markup",
        "created_at", "closed_at", "last_activity_at",
        "interactions", "win", "deal_stage.name", "user.id", "user.name",
        "deal_lost_reason.name","Tipo de Contato", "Fonte de Contato" , "Tipo de Obra"   
    ]
    
    df_rep = df[df['user.name'].isin(['Bruno Crispim', 'Gabriel  Bento'])]
    df_rep = df_rep[colunas].copy()
    df_rep.loc[:, "Fator"] = (
        df_rep["Fator"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float, errors="ignore")
    )
    
    total_orc = len(df_rep[df_rep["deal_stage.name"].isin(["Venda Ganha", "Venda Perdida", "Venda Cancelada"])])

    taxa_conversão_rep = df_rep[df_rep["deal_stage.name"] == "Venda Ganha"].shape[0]/total_orc
    df_rep['Fator'] = pd.to_numeric(df_rep['Fator'], errors='coerce')
    df_rep['Fator'] = df_rep['Fator'].astype(float)
    
    estagios_validos = ['Venda Ganha',"Venda Perdida", "Venda Cancelada"]
    df_validos = df_rep[df_rep["deal_stage.name"].isin(estagios_validos)] 
    total = df_validos.groupby("organization.name").size()
    ganhas = df_validos[df_validos['deal_stage.name']== "Venda Ganha"].groupby('organization.name').size()
    taxa_conversao = (ganhas / total)
    df_rep["taxa_conversao"] = df["organization.name"].map(taxa_conversao)
    
    
    df_ganho_mes = df_rep[(df_rep['deal_stage.name'] == 'Venda Ganha') & df_rep['closed_at'].notna()]
    df_ganho_mes['closed_at'] = pd.to_datetime(df['closed_at'])
    df_ganho_mes['ano_mes'] = df_ganho_mes['closed_at'].dt.to_period('M')
    faturamento_mensal = df_ganho_mes.groupby('ano_mes')['amount_total'].sum().reset_index()

    faturamento_mensal['ano_mes'] = faturamento_mensal['ano_mes'].astype(str)

    faturamento_mensal['faturamento_mes_anterior'] = faturamento_mensal['amount_total'].shift(1)
    faturamento_mensal['diferenca'] = (
        faturamento_mensal['amount_total'] - faturamento_mensal['faturamento_mes_anterior']
    )
    faturamento_mensal['crescimento_percentual'] = (
        faturamento_mensal['diferenca'] / faturamento_mensal['faturamento_mes_anterior']
    ).fillna(0)

    faturamento_mensal['dif_meta'] = faturamento_mensal['amount_total'] - 1500000


    faturamento_mensal.to_excel(r"C:\Users\Orçamento\ONE DRIVE ORCAMENTO\OneDrive - GRUPO RETEC\02. Engenharia\Dep. Orçamentos\POWERBI\AUTOMACAO RD\data\faturamento_mensal.xlsx", index=False)
    
    
    caminho_rep = r"C:\Users\Orçamento\ONE DRIVE ORCAMENTO\OneDrive - GRUPO RETEC\02. Engenharia\Dep. Orçamentos\POWERBI\AUTOMACAO RD\data\negociacoes_rep_2025.xlsx"
    df_rep.to_excel(caminho_rep)