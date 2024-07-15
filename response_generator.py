def generate_response(intent, text):
    responses = {
        "PLACE_ORDER": "Sure, I can help you place an order. What would you like to buy?",
        "ACCOUNT_INQUIRY": "Your account balance is $1,500. Is there anything else you need?",
        "TECH_SUPPORT": "I can assist you with technical support. Can you describe the issue?"
    }
    return responses.get(intent, "I'm not sure how to help with that.")
