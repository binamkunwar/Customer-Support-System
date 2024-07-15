from intent_classifier import get_intent
from response_generator import generate_response

class DialogueManager:
    def __init__(self):
        self.state = {}

    def update_state(self, user_input):
        self.state['last_intent'] = get_intent(user_input)

    def get_response(self, user_input):
        intent = get_intent(user_input)
        self.update_state(user_input)
        return generate_response(intent, user_input)
