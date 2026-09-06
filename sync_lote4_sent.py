import sqlite3
import json
import os
from datetime import datetime

DB_PATH = 'prospector.db'
DASHBOARD_PATH = 'dashboard.html'
DATA_PROPOSTA = "2026-09-04 20:25"

lote4_enviados = [
    {
        "slug": "future-auto-care",
        "status": "proposta enviada",
        "dataProposta": DATA_PROPOSTA,
        "obs": "Proposta personalizada com novo site em tema Dark Mode enviada em 04/09/2026 às 20:25 via Gmail (andre1981luiz@gmail.com). Chácara Santo Antônio."
    },
    {
        "slug": "simone-moveis-planejados",
        "status": "proposta enviada",
        "dataProposta": DATA_PROPOSTA,
        "obs": "Proposta personalizada com novo site estilo arquitetura e foco em planta no WhatsApp enviada em 04/09/2026 às 20:25 via Gmail. Zona Sul / Sto. Amaro."
    },
    {
        "slug": "tempstar-ar-condicionado",
        "status": "proposta enviada",
        "dataProposta": DATA_PROPOSTA,
        "obs": "Proposta personalizada com destaque para laudos PMOC e botão de emergência enviada em 04/09/2026 às 20:25 via Gmail. Rua São Benedito, Santo Amaro."
    }
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for lead in lote4_enviados:
    cursor.execute('''
        UPDATE leads SET 
            status = ?, dataProposta = ?, obs = ?,
            atualizado = datetime('now','localtime')
        WHERE slug = ?
    ''', (lead['status'], lead['dataProposta'], lead['obs'], lead['slug']))
    print(f"Banco atualizado: {lead['slug']} -> {lead['status']}")

conn.commit()

# Recuperar todos os leads ordenados
cursor.execute('SELECT * FROM leads')
cols = [col[0] for col in cursor.description]
todos_leads = []
for row in cursor.fetchall():
    d = dict(zip(cols, row))
    todos_leads.append(d)

conn.close()

# Atualizar o dashboard.html (snapshot JSON)
if os.path.exists(DASHBOARD_PATH):
    with open(DASHBOARD_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    ini_tag = '<script id="dados" type="application/json">'
    fim_tag = '</script>'
    ini = html.find(ini_tag)
    if ini != -1:
        ini += len(ini_tag)
        fim = html.find(fim_tag, ini)
        if fim != -1:
            novo_json = {
                "atualizado": "04/09/2026 às 20:25",
                "leads": todos_leads
            }
            json_str = json.dumps(novo_json, ensure_ascii=False, indent=2)
            novo_html = html[:ini] + "\n" + json_str + "\n" + html[fim:]
            with open(DASHBOARD_PATH, 'w', encoding='utf-8') as f:
                f.write(novo_html)
            print("dashboard.html atualizado com sucesso!")

print("Sincronização de envio do Lote 4 concluída!")
