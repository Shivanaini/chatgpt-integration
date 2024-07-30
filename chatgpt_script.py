import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Hello, ChatGPT!"
    response = chat_with_gpt(prompt)
    print("ChatGPT Response:", response)
