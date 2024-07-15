from transformers import pipeline

classifier = pipeline('text-classification', model='bert-base-uncased')

def classify_intent(text):
    result = classifier(text)
    return result[0]['label']

# Example intents
intents = {
    "PLACE_ORDER": ["I want to place an order", "Order a product"],
    "ACCOUNT_INQUIRY": ["What is my account balance?", "Check my account status"],
    "TECH_SUPPORT": ["I need help with my device", "My internet is not working"]
}

def get_intent(text):
    for intent, phrases in intents.items():
        for phrase in phrases:
            if phrase in text:
                return intent
    return "UNKNOWN_INTENT"
