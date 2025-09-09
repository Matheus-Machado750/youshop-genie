CTA_WORDS = ["inscreva", "compre", "clique", "garanta", "saiba", "quero"]

def score_text(text: str) -> int:
    """Calcula score básico do texto"""
    score = 0
    length = len(text)
    if 40 <= length <= 160:
        score += 30
    lower = text.lower()
    if any(w in lower for w in CTA_WORDS):
        score += 30
    score += text.count("!") * 5
    return score

def predict_best_version(texts):
    """Retorna o melhor texto com base no score"""
    if not texts:
        return "Nenhum texto gerado"
    best = max(texts, key=score_text)
    return best