# ============================================================
# Project 1 - Sentiment Analysis
# Hexasoftware Internship
# ============================================================
import re

POSITIVE_WORDS = {
    "good","great","excellent","amazing","wonderful","fantastic",
    "love","best","happy","awesome","superb","outstanding","brilliant",
    "positive","perfect","nice","beautiful","enjoy","recommend","helpful",
    "pleased","satisfied","delighted","impressive","incredible","exceptional"
}

NEGATIVE_WORDS = {
    "bad","terrible","horrible","worst","hate","awful","poor","boring",
    "disappointing","useless","waste","broken","ugly","annoying","angry",
    "sad","negative","problem","issue","fail","failure","lousy",
    "disgusting","dreadful","unacceptable","frustrated","pathetic"
}

NEGATION_WORDS = {"not","no","never","cannot","can't","don't","doesn't"}

def analyze_sentiment(text: str) -> dict:
    tokens = re.findall(r"\b\w+\b", text.lower())
    pos_score, neg_score, negated = 0, 0, False
    for token in tokens:
        if token in NEGATION_WORDS:
            negated = True; continue
        if token in POSITIVE_WORDS:
            if negated: neg_score += 1
            else: pos_score += 1
        elif token in NEGATIVE_WORDS:
            if negated: pos_score += 1
            else: neg_score += 1
        negated = False
    total = pos_score + neg_score
    if total == 0: label, conf = 'Neutral', 50.0
    elif pos_score > neg_score: label, conf = 'Positive', round(pos_score/total*100,2)
    else: label, conf = 'Negative', round(neg_score/total*100,2)
    return {'text':text,'label':label,'pos_score':pos_score,'neg_score':neg_score,'confidence':conf}

samples = [
    "The product is absolutely amazing and I love it!",
    "This is the worst service I have ever experienced.",
    "The weather today is okay.",
    "I am not happy with the quality of this product.",
    "Excellent performance and outstanding customer support!",
    "The movie was boring and a complete waste of time.",
    "It works fine, nothing special about it.",
    "I would highly recommend this, it is brilliant!",
    "Terrible experience, I am very frustrated and angry.",
    "The food was great but the service was a bit slow."
]

print("="*65)
print("PROJECT 1 - SENTIMENT ANALYSIS RESULTS")
print("Hexasoftware Internship")
print("="*65)

for i, sample in enumerate(samples, 1):
    r = analyze_sentiment(sample)
    print(f'[{i}] {r["text"]}')
    print(f'    Sentiment: {r["label"]} | Confidence: {r["confidence"]}%')

print("="*65)
