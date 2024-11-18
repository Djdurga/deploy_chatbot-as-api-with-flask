from transformers import pipeline

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Simulate chatbot response (replace with your own logic)
def chatbot_response(user_input):
    # Placeholder for actual chatbot response logic
    return f"You said: {user_input}"

# Analyze sentiment
def analyze_sentiment(user_input):
    sentiment = sentiment_analyzer(user_input)[0]
    return sentiment['label'], sentiment['score']

# Main interaction function
def interact_with_user():
    # Get user input
    user_input = input("You: ")

    # Analyze the sentiment of the user's message
    label, score = analyze_sentiment(user_input)

    # If the sentiment is negative, respond empathetically
    if label == "NEGATIVE":
        empathetic_message = "I'm sorry you're feeling this way. How can I help?"
        print(f"Bot: {empathetic_message}")
    else:
        # Otherwise, respond with a normal chatbot reply
        print(f"Bot: {chatbot_response(user_input)}")

# Run the interaction
if __name__ == "__main__":
    interact_with_user()

