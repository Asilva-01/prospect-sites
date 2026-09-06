import sqlite3
import json
import os

DB_PATH = 'prospector.db'
DASHBOARD_PATH = 'dashboard.html'

leads_enviados_hoje = [
    {
        "slug": "cecilia-freytas-psico",
        "nome": "Dra. Cecília Freytas — Psicóloga",
        "nicho": "psicologos",
        "cidade": "Santo Amaro, São Paulo - SP",
        "nota": 5.0,
        "avaliacoes": 70,
        "email": "contato@ceciliafreytas.com.br",
        "telefone": "(11) 99601-2736",
        "whatsapp": "5511996012736",
        "siteAntigo": "https://ceciliafreytas.com.br/",
        "motivo": "Menu oculto no celular abaixo de 992px, carregamento lento de fotos e sem FAQ de quebra de objeções",
        "status": "proposta enviada",
        "urlNova": "https://asilva-01.github.io/prospect-sites/sites/cecilia-freytas-psico/",
        "dataProposta": "2026-09-02 20:00",
        "valor": 1200.0,
        "obs": "Abordagem com sugestão para o site enviada em 02/09/2026. Consultório no NovAmérica Office Park.",
        "contratoStatus": "pendente",
        "contratoEm": "",
        "manutencao": 150.0,
        "pago": 0,
        "docCliente": "",
        "endCliente": "Av. das Nações Unidas, 18801 - NovAmérica Office Park, Santo Amaro, São Paulo - SP"
    },
    {
        "slug": "metra-psicologia",
        "nome": "Métra Psicologia e Psicanálise",
        "nicho": "psicologos",
        "cidade": "Santo Amaro, São Paulo - SP",
        "nota": 4.8,
        "avaliacoes": 35,
        "email": "contato@metrapsi.com.br",
        "telefone": "(11) 999970-6712",
        "whatsapp": "5511999706712",
        "siteAntigo": "https://metrapsi.com.br/",
        "motivo": "Carregamento inicial pesado, cartões de profissionais desalinhados no celular",
        "status": "proposta enviada",
        "urlNova": "https://asilva-01.github.io/prospect-sites/sites/metra-psicologia/",
        "dataProposta": "2026-09-02 20:00",
        "valor": 1200.0,
        "obs": "Abordagem com sugestão para o site enviada em 02/09/2026. Clínica tradicional na Alexandre Dumas.",
        "contratoStatus": "pendente",
        "contratoEm": "",
        "manutencao": 150.0,
        "pago": 0,
        "docCliente": "",
        "endCliente": "Rua Alexandre Dumas, 501 - Chácara Santo Antônio, São Paulo - SP"
    },
    {
        "slug": "clinica-langner",
        "nome": "Clínica Langner Psicologia e Neuropsicologia",
        "nicho": "psicologos",
        "cidade": "Santo Amaro, São Paulo - SP",
        "nota": 4.9,
        "avaliacoes": 28,
        "email": "contato@clinicalangner.com.br",
        "telefone": "(11) 94818-9898",
        "whatsapp": "5511948189898",
        "siteAntigo": "https://clinicalangner.com.br/",
        "motivo": "Visual poluído no mobile com informações concorrentes, ficha de agendamento oculta no celular",
        "status": "proposta enviada",
        "urlNova": "https://asilva-01.github.io/prospect-sites/sites/clinica-langner/",
        "dataProposta": "2026-09-02 20:00",
        "valor": 1200.0,
        "obs": "Abordagem com sugestão para o site enviada em 02/09/2026. Manoel Borba, Centro de Santo Amaro.",
        "contratoStatus": "pendente",
        "contratoEm": "",
        "manutencao": 150.0,
        "pago": 0,
        "docCliente": "",
        "endCliente": "Rua Manoel Borba, 292 - Centro de Santo Amaro, São Paulo - SP"
    },
    {
        "slug": "paula-paraiso-nutri",
        "nome": "Dra. Paula Paraíso Nutricionista",
        "nicho": "nutricionistas",
        "cidade": "Santo Amaro, São Paulo - SP",
        "nota": 5.0,
        "avaliacoes": 138,
        "email": "contato@paulaparaiso.com.br",
        "telefone": "(11) 96277-7356",
        "whatsapp": "5511962777356",
        "siteAntigo": "https://paulaparaiso.com.br/",
        "motivo": "Carregamento lento no 4G/5G, navegação antiga e quebrada no mobile",
        "status": "proposta enviada",
        "urlNova": "https://asilva-01.github.io/prospect-sites/sites/paula-paraiso-nutri/",
        "dataProposta": "2026-09-02 20:00",
        "valor": 1200.0,
        "obs": "Abordagem com sugestão para o site enviada em 02/09/2026. Consultório na Vila Prel.",
        "contratoStatus": "pendente",
        "contratoEm": "",
        "manutencao": 150.0,
        "pago": 0,
        "docCliente": "",
        "endCliente": "Rua Itirapuã, 218 - Vila Prel / Zona Sul, São Paulo - SP"
    },
    {
        "slug": "luciene-hessel-psico",
        "nome": "Luciene Hessel Fogaça — Psicóloga",
        "nicho": "psicologos",
        "cidade": "São Paulo - SP",
        "nota": 5.0,
        "avaliacoes": 10,
        "email": "contato@psicologaluciene.com.br",
        "telefone": "(11) 97018-4141",
        "whatsapp": "5511970184141",
        "siteAntigo": "https://psicologaluciene.com.br/",
        "motivo": "Erro visível no rodapé ('Error: Cant get content') e texto desconexo fora de contexto no meio da página",
        "status": "proposta enviada",
        "urlNova": "https://asilva-01.github.io/prospect-sites/sites/luciene-hessel-psico/",
        "dataProposta": "2026-09-02 20:00",
        "valor": 1200.0,
        "obs": "Abordagem com sugestão para o site enviada em 02/09/2026. Brooklin Velho / Campo Belo.",
        "contratoStatus": "pendente",
        "contratoEm": "",
        "manutencao": 150.0,
        "pago": 0,
        "docCliente": "",
        "endCliente": "Rua Lacedemônia, Brooklin Velho, São Paulo - SP"
    },
    {
        "slug": "bianca-cremonez-nutri",
        "nome": "Bianca Cremonez Magnelli — Nutricionista",
        "nicho": "nutricionistas",
        "cidade": "São Paulo - SP",
        "nota": 5.0,
        "avaliacoes": 15,
        "email": "nutricionista@nutricionistasp.com",
        "telefone": "(11) 97232-7220",
        "whatsapp": "5511972327220",
        "siteAntigo": "http://www.nutricionistasp.com/",
        "motivo": "Marca dividida em dois endereços; site HTTP antigo sem SSL exibindo alerta de 'não seguro'",
        "status": "proposta enviada",
        "urlNova": "https://asilva-01.github.io/prospect-sites/sites/bianca-cremonez-nutri/",
        "dataProposta": "2026-09-02 20:00",
        "valor": 1200.0,
        "obs": "Abordagem com sugestão para o site enviada em 02/09/2026. Consultório em Moema.",
        "contratoStatus": "pendente",
        "contratoEm": "",
        "manutencao": 150.0,
        "pago": 0,
        "docCliente": "",
        "endCliente": "Av. Moaci, 857 - Moema, São Paulo - SP"
    },
    {
        "slug": "clinica-equilibrio-psico",
        "nome": "Clínica Equilíbrio — Psicologia e Neuropsicologia",
        "nicho": "psicologos",
        "cidade": "São Paulo - SP",
        "nota": 5.0,
        "avaliacoes": 12,
        "email": "contato@equilibriopsiconeuro.com.br",
        "telefone": "(11) 99996-0772",
        "whatsapp": "5511999960772",
        "siteAntigo": "https://equilibriopsiconeuro.com.br/",
        "motivo": "Template antigo Wix, rodapé com ano desatualizado e elementos desalinhados na tela móvel",
        "status": "proposta enviada",
        "urlNova": "https://asilva-01.github.io/prospect-sites/sites/clinica-equilibrio-psico/",
        "dataProposta": "2026-09-02 20:00",
        "valor": 1200.0,
        "obs": "Abordagem com sugestão para o site enviada em 02/09/2026. Moema.",
        "contratoStatus": "pendente",
        "contratoEm": "",
        "manutencao": 150.0,
        "pago": 0,
        "docCliente": "",
        "endCliente": "Alameda dos Arapanés, 881 - cj 33, Moema, São Paulo - SP"
    }
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

CAMPOS = ['slug','nome','nicho','cidade','nota','avaliacoes','email','telefone','whatsapp',
          'siteAntigo','motivo','status','urlNova','dataProposta','valor','obs',
          'contratoStatus','contratoEm','manutencao','pago','docCliente','endCliente']

for lead in leads_enviados_hoje:
    cursor.execute('SELECT slug FROM leads WHERE slug = ?', (lead['slug'],))
    existe = cursor.fetchone()
    if existe:
        cursor.execute('''
            UPDATE leads SET 
                status = ?, dataProposta = ?, valor = ?, manutencao = ?, obs = ?,
                email = ?, telefone = ?, whatsapp = ?, urlNova = ?, motivo = ?,
                atualizado = datetime('now','localtime')
            WHERE slug = ?
        ''', (
            lead['status'], lead['dataProposta'], lead['valor'], lead['manutencao'], lead['obs'],
            lead['email'], lead['telefone'], lead['whatsapp'], lead['urlNova'], lead['motivo'],
            lead['slug']
        ))
        print(f"Atualizado: {lead['slug']}")
    else:
        cursor.execute(f'''
            INSERT INTO leads ({','.join(CAMPOS)}) VALUES ({','.join('?'*len(CAMPOS))})
        ''', [lead.get(k, '') for k in CAMPOS])
        print(f"Inserido: {lead['slug']}")

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
                "atualizado": "02/09/2026 às 20:00",
                "leads": todos_leads
            }
            json_str = json.dumps(novo_json, ensure_ascii=False, indent=2)
            novo_html = html[:ini] + "\n" + json_str + "\n" + html[fim:]
            with open(DASHBOARD_PATH, 'w', encoding='utf-8') as f:
                f.write(novo_html)
            print("dashboard.html atualizado com sucesso!")

print("Processo concluído com sucesso!")
