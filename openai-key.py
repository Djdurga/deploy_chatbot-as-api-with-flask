import openai

# Set up your OpenAI API key
openai.api_key = 'c1b0pL5SnW063O6YIVqSFkN1HHL3r2vW6U0kFV4s9-p-82kCkBqEf-Cc-shhCKf_uGSKXM6jjsT3BlbkFJ0_Ulh4bg5NFUarawwJyEdrmozm3vVHqxDJvCHKjkIM9dAiTCW2CoNuRtnIYf9R6ieGwh0YFA8A'

def chatbot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with your model (e.g., "gpt-3.5-turbo")
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

# Example interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    print(f"Bot: {chatbot_response(user_input)}")
