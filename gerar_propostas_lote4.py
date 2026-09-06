import urllib.parse

remetente = "andre1981luiz@gmail.com"

leads = [
    {
        "slug": "future-auto-care",
        "nome": "Future Auto Care",
        "to": "futureautocare.oficial@gmail.com",
        "su": "Future Auto Care, posso mostrar uma sugestão para o site?",
        "body": """Olá, pessoal da Future Auto Care, tudo bem?

Acompanho o trabalho de vocês na Chácara Santo Antônio e me chamou a atenção o nível técnico nos serviços de vitrificação cerâmica, PPF e o cuidado impecável com veículos de alto padrão.

Ao pesquisar o site oficial de vocês pelo celular, notei que a página tem um carregamento pesado e um visual claro que não valoriza o brilho e a sofisticação dos carros que vocês atendem — o que pode fazer donos de veículos premium desistirem do contato antes de pedir um orçamento.

Como trabalho com criação de páginas de alta conversão para estética automotiva, tomei a liberdade de criar uma nova versão exclusiva em tema dark premium para a Future Auto Care, rápida no celular e pensada para direcionar o cliente direto ao WhatsApp:
https://asilva-01.github.io/prospect-sites/sites/future-auto-care/

Dê uma olhada (inclusive pelo smartphone) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    },
    {
        "slug": "simone-moveis-planejados",
        "nome": "Simone Móveis Planejados",
        "to": "simonemoveisplanejados@gmail.com",
        "su": "Simone Móveis, posso mostrar uma sugestão para o site?",
        "body": """Olá, equipe da Simone Móveis Planejados, tudo bem?

Acompanho os projetos sob medida de vocês na Zona Sul e acho impecável o acabamento e o bom gosto das cozinhas e dormitórios planejados que produzem.

Vi que vocês divulgam a marca na região, mas ao abrir o site oficial no celular notei que a galeria de fotos demora para abrir e há um pequeno erro de digitação no título da página no Google. Em móveis de alto padrão, onde o cliente decide pelo impacto visual, isso pode fazer muitas pessoas desistirem antes de pedir uma cotação.

Como trabalho com criação de páginas de alta conversão para marcenarias e lojas de planejados, desenhei uma nova versão moderna e elegante para a Simone Móveis, com visual de arquitetura e foco em fazer o cliente enviar a planta do imóvel direto para o WhatsApp:
https://asilva-01.github.io/prospect-sites/sites/simone-moveis-planejados/

Dê uma olhada (inclusive pelo smartphone) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    },
    {
        "slug": "tempstar-ar-condicionado",
        "nome": "Tempstar Ar Condicionado",
        "to": "tempstar@tempstar.com.br",
        "su": "Tempstar, posso mostrar uma sugestão para o site de vocês?",
        "body": """Olá, pessoal da Tempstar, tudo bem?

Encontrei a empresa de vocês aqui em Santo Amaro (na Rua São Benedito) e me chamou a atenção a tradição técnica no atendimento de climatização e a especialização em contratos de PMOC para empresas.

Ao buscar o site oficial no celular, percebi que a página demora para carregar os menus e contatos técnicos. Em climatização, clientes residenciais com calor/urgência ou empresas precisando de suporte querem contato imediato, e a lentidão pode levá-los a ligar para outro prestador.

Como trabalho com páginas de alta conversão para o setor técnico, desenvolvi uma nova versão moderna e ultrarrápida para a Tempstar, com botão de emergência em 1 toque e destaque para os laudos e contratos de PMOC:
https://asilva-01.github.io/prospect-sites/sites/tempstar-ar-condicionado/

Dê uma olhada (inclusive pelo smartphone) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    }
]

if __name__ == "__main__":
    with open("urls_gmail_lote4.txt", "w", encoding="utf-8") as f:
        for l in leads:
            params = urllib.parse.urlencode({'view': 'cm', 'fs': '1', 'to': l['to'], 'su': l['su'], 'body': l['body']}, quote_via=urllib.parse.quote)
            url = f"https://mail.google.com/mail/u/{remetente}/?{params}"
            f.write(f"=== {l['nome']} ===\n")
            f.write(f"Para: {l['to']}\n")
            f.write(f"Assunto: {l['su']} ({len(l['su'])} caracteres)\n")
            f.write(f"Palavras no corpo: {len(l['body'].split())}\n")
            f.write(f"URL Gmail:\n{url}\n\n")
            print(f"Gerado para {l['nome']} - {len(l['body'].split())} palavras - Assunto: {len(l['su'])} caracteres")
    print("\nArquivo urls_gmail_lote4.txt gerado com sucesso!")
