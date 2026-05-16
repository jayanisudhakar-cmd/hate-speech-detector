# app.py
from transformers import pipeline

hate_detector = pipeline("text-classification", model="martin-ha/toxic-comment-model")
nsfw_detector = pipeline("text-classification", model="michellejieli/NSFW_text_classifier")
vulgar_keywords = ["spend a night", "hookup", "nudes", "sexy", "sugar daddy"]

while True:
    text = input("Enter comment (or 'exit' to stop): ")
    if text.lower() == 'exit': break
    
    is_hate = hate_detector(text)[0]['label'] == 'toxic'
    is_nsfw = nsfw_detector(text)[0]['label'] == 'NSFW'
    has_vulgar_keyword = any(word in text.lower() for word in vulgar_keywords)
    
    if is_hate or is_nsfw or has_vulgar_keyword:
        print("❌ Blocked: Hate speech or vulgar content detected.\n")
    else:
        print("✅ Approved: Comment posted.\n")