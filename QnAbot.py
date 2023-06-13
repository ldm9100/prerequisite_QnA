import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    content = input("Q: ")

    response = openai.Completion.create(
        model="curie:ft-personal-2023-06-12-17-22-44",
        prompt= "\nQ: " + content + "\nA: ",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )

    chat_response = response.choices[0].text.strip()
    print(f"A: {chat_response}")
