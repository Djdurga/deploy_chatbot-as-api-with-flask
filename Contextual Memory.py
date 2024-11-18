import openai

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chatbot_response(user_input):
    conversation.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation
    )
    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return response['choices'][0]['message']['content']
