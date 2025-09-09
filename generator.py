import random

# Templates de conteúdo
POST_TEMPLATES = [
    "🚀 Quer transformar tempo livre em renda? {product} é prático e direto. Comece hoje!",
    "Precisa de resultados reais? {product} ajuda {audience} a montar campanhas inteligentes.",
    "🔑 Controle e resultado: aprenda com {product} e aumente suas vendas como afiliado."
]

DESC_TEMPLATES = [
    "{product} foi criado para {audience}. Aprenda a organizar campanhas, acompanhar métricas e aumentar a conversão.",
    "Curso prático de {product} para {audience}. Aulas objetivas, exercícios aplicáveis e templates prontos para uso.",
    "Aprenda técnicas práticas e diretas com {product}: planilhas, indicadores e passos para vendas consistentes."
]

EMAIL_SUBJECT_TEMPLATES = [
    "Aprenda {product} e venda mais como afiliado 🚀",
    "Transforme seu tempo em renda com {product}",
    "{product}: o passo prático para melhorar suas vendas"
]

EMAIL_BODY_TEMPLATES = [
    "Olá {name},\n\nVocê já pensou em como {product} pode transformar sua forma de vender online? Nosso curso prático para {audience} ensina a organizar campanhas e usar dados para vender mais.\n\n[CTA: Quero Aprender]",
    "Oi {name},\n\nCom {product} você aprende planilhas e rotinas que ajudam afiliados iniciantes a montar campanhas que convertem. Sem teoria excessiva — só prática.\n\nGaranta sua vaga!"
]

# Funções simples chamadas pelo main.py
def generate_post(product: str, audience: str = "afiliados"):
    return random.choice(POST_TEMPLATES).format(product=product, audience=audience)

def generate_description(product: str, audience: str = "afiliados"):
    return random.choice(DESC_TEMPLATES).format(product=product, audience=audience)

def generate_email(product: str, audience: str = "afiliados", name: str = "amigo"):
    subject = random.choice(EMAIL_SUBJECT_TEMPLATES).format(product=product)
    body = random.choice(EMAIL_BODY_TEMPLATES).format(product=product, audience=audience, name=name)
    return f"**{subject}**\n\n{body}"