import urllib.parse

leads = [
    {
        "nome": "Dra. Paula Paraíso",
        "email": "contato@paulaparaiso.com.br",
        "su": "Dra. Paula, posso te mostrar uma sugestão para o seu site?",
        "body": """Olá, Dra. Paula, tudo bem?

Encontrei seu trabalho em Santo Amaro / Vila Prel com avaliação máxima de 5.0 estrelas no Google e me chamou a atenção o reconhecimento dos seus pacientes nas mais de 138 avaliações sobre emagrecimento saudável e nutrição clínica.

Ao buscar seu site oficial, vi que sua página atual tem um carregamento lento no celular e uma estrutura mais antiga, o que não transmite a exclusividade e a modernidade que a sua autoridade merece.

Como trabalho com criação de páginas para profissionais de saúde, criei uma versão exclusiva e moderna para você, com foco total em valorizar suas especialidades, convênios e converter visitantes em agendamentos no seu WhatsApp.

Você pode conferir a nova versão já no ar por aqui:
https://asilva-01.github.io/prospect-sites/sites/paula-paraiso-nutri/

Dê uma olhada (inclusive pelo celular) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    },
    {
        "nome": "Métra Psicologia",
        "email": "contato@metrapsi.com.br",
        "su": "Métra Psicologia, posso mostrar uma sugestão para o site de vocês?",
        "body": """Olá, pessoal da Métra Psicologia, tudo bem?

Encontrei a clínica de vocês na Chácara Santo Antônio com excelente nota no Google e me chamou a atenção os mais de 25 anos de história e tradição no atendimento em psicanálise e psicoterapia.

Ao buscar o site oficial de vocês pelo celular, vi que a página tem um carregamento pesado e os cartões de profissionais ficam desalinhados na tela móvel, o que pode afastar pacientes que buscam atendimento pelo smartphone.

Como trabalho com criação de páginas para profissionais e clínicas de saúde, criei uma versão exclusiva e moderna para a Métra, com foco total em valorizar a equipe, a tradição da clínica e facilitar os agendamentos no WhatsApp.

Você pode conferir a nova versão já no ar por aqui:
https://asilva-01.github.io/prospect-sites/sites/metra-psicologia/

Dê uma olhada (inclusive pelo celular) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    },
    {
        "nome": "Clínica Langner",
        "email": "contato@clinicalangner.com.br",
        "su": "Dr. Langner, posso te mostrar uma sugestão para o site da clínica?",
        "body": """Olá, Dr. Langner e equipe, tudo bem?

Encontrei a Clínica Langner em Santo Amaro com excelente avaliação de 4.9 estrelas no Google e me chamou a atenção o carinho e a seriedade nos relatos de pacientes sobre os atendimentos em neuropsicologia e psicologia clínica.

Ao navegar pelo site oficial no celular, vi que a página concentra muitas informações e cores misturadas na primeira tela, o que acaba escondendo a ficha de agendamentos para quem chega através do smartphone.

Como trabalho com criação de páginas para profissionais de saúde, criei uma versão exclusiva e moderna para a clínica, com foco total em valorizar a avaliação neuropsicológica e converter visitantes em agendamentos no seu WhatsApp.

Você pode conferir a nova versão já no ar por aqui:
https://asilva-01.github.io/prospect-sites/sites/clinica-langner/

Dê uma olhada (inclusive pelo celular) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    },
    {
        "nome": "Bianca Cremonez",
        "email": "nutricionista@nutricionistasp.com",
        "su": "Bianca, posso te mostrar uma sugestão para o seu site?",
        "body": """Olá, Bianca, tudo bem?

Encontrei seu trabalho como nutricionista esportiva em Moema e achei excelente a sua trajetória focada em hipertrofia, emagrecimento e performance para atletas e praticantes de atividade física.

Ao buscar seu site oficial, notei que sua presença está dividida em dois endereços e um deles ainda roda sem certificado de segurança (HTTP), o que dispara aviso de "site não seguro" no navegador de quem acessa pelo celular.

Como trabalho com criação de páginas para profissionais de saúde, criei uma versão exclusiva, unificada e moderna para você, com foco total em valorizar suas especialidades e converter visitantes em agendamentos no seu WhatsApp.

Você pode conferir a nova versão já no ar por aqui:
https://asilva-01.github.io/prospect-sites/sites/bianca-cremonez-nutri/

Dê uma olhada (inclusive pelo celular) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    },
    {
        "nome": "Dra. Cecília Freytas",
        "email": "contato@ceciliafreytas.com.br",
        "su": "Dra. Cecília, posso te mostrar uma sugestão para o seu site?",
        "body": """Olá, Dra. Cecília, tudo bem?

Encontrei seu trabalho no NovAmérica Office Park em Santo Amaro com avaliação máxima de 5.0 estrelas no Google e me chamou a atenção os mais de 70 depoimentos elogiando o acolhimento e a escuta no seu consultório.

Ao buscar seu site oficial no celular, vi que o menu de navegação acaba sumindo em telas menores e as fotos demoram para carregar, o que pode dificultar a vida de pacientes que buscam agendar uma sessão.

Como trabalho com criação de páginas para profissionais de saúde, criei uma versão exclusiva e moderna para você, com foco total em transmitir acolhimento e converter visitantes em agendamentos no seu WhatsApp.

Você pode conferir a nova versão já no ar por aqui:
https://asilva-01.github.io/prospect-sites/sites/cecilia-freytas-psico/

Dê uma olhada (inclusive pelo celular) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    },
    {
        "nome": "Luciene Hessel",
        "email": "contato@psicologaluciene.com.br",
        "su": "Luciene, posso te mostrar uma sugestão para o seu site?",
        "body": """Olá, Luciene, tudo bem?

Encontrei seu consultório de psicologia na região do Brooklin Velho e Campo Belo e achei excelente sua atuação com atendimento clínico presencial e online.

Ao buscar seu site oficial no celular, notei que o rodapé está exibindo uma mensagem de erro ("Error: Cant get content") e há um texto sobre relógios fora de contexto no meio da página, o que parece ser uma falha técnica do tema antigo que passa desconfiança a novos pacientes.

Como trabalho com criação de páginas para profissionais de saúde, criei uma versão exclusiva, limpa e moderna para você, sem nenhum desses problemas e com foco total em converter visitantes em agendamentos no seu WhatsApp.

Você pode conferir a nova versão já no ar por aqui:
https://asilva-01.github.io/prospect-sites/sites/luciene-hessel-psico/

Dê uma olhada (inclusive pelo celular) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    },
    {
        "nome": "Clínica Equilíbrio",
        "email": "contato@equilibriopsiconeuro.com.br",
        "su": "Clínica Equilíbrio, posso mostrar uma sugestão para o site de vocês?",
        "body": """Olá, pessoal da Clínica Equilíbrio, tudo bem?

Encontrei a clínica de vocês em Moema e achei excelente a atuação multidisciplinar integrando psicologia clínica, psicoterapia infantil e avaliação neuropsicológica.

Ao buscar o site oficial no celular, percebi que a página usa um template antigo com elementos desalinhados na tela móvel e o rodapé desatualizado, o que não transmite toda a modernidade e cuidado da clínica.

Como trabalho com criação de páginas para profissionais e clínicas de saúde, criei uma versão exclusiva e moderna para a Equilíbrio, com foco total em valorizar os atendimentos e converter visitantes em agendamentos no WhatsApp.

Você pode conferir a nova versão já no ar por aqui:
https://asilva-01.github.io/prospect-sites/sites/clinica-equilibrio-psico/

Dê uma olhada (inclusive pelo celular) e me diga o que achou!

Abraços,
André Luiz da Silva
Designer de páginas de alta conversão
WhatsApp: (11) 98239-5014"""
    }
]

with open("urls_gmail.txt", "w", encoding="utf-8") as f:
    for l in leads:
        params = urllib.parse.urlencode({'view': 'cm', 'fs': '1', 'to': l['email'], 'su': l['su'], 'body': l['body']}, quote_via=urllib.parse.quote)
        url = f"https://mail.google.com/mail/u/andre1981luiz@gmail.com/?{params}"
        f.write(f"=== {l['nome']} ===\n")
        f.write(f"{url}\n\n")
print("URLs geradas com sucesso em urls_gmail.txt")
