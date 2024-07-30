import spacy

nlp = spacy.load("en_core_web_sm")

# Define a dictionary to store the chatbot's responses
responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hello! What's on your mind?",
    "how are you": "I'm doing well, thanks! How about you?",
    "what's your name": "I'm Chatty, nice to meet you!",
    "goodbye": "See you later! Have a great day!",
    "thanks": "You're welcome!",
    "none": "I didn't understand that. Can you please rephrase?"
}

# Define a function to process user input
def process_input(user_input):
    doc = nlp(user_input.lower())
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return responses["what's your name"]
    for token in doc:
        if token.lemma_ in responses:
            return responses[token.lemma_]
    return responses["none"]

# Create a chatbot class
class Chatbot:
    def _init_(self):
        self.user_input = ""

    def start_conversation(self):
        print("Welcome to Chatty! I'm here to help.")
        while True:
            self.user_input = input("You: ")
            response = process_input(self.user_input)
            print("Chatty: " + response)

# Create an instance of the chatbot and start the conversation
chatbot = Chatbot()
chatbot.start_conversation()
