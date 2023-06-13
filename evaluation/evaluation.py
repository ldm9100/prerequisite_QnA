import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

model_name = "curie:ft-personal-2023-06-12-17-22-44"

with open('questions.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]  # Ignore empty lines

questions = []

for i in range(0, len(lines), 2):  # Skip one line each time because one question takes up two lines
    context, q_line = lines[i], lines[i+1]
    
    # Combine the context and question
    question = context + " " + q_line
    questions.append(question)

qa_pairs = []

for question in questions:
    response = openai.Completion.create(
        model=model_name,
        prompt=question + "\nA: ",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    qa_pairs.append({
        'question': question,
        'answer': response.choices[0].text.strip()
    })

with open('eval.json', 'w') as f:
    json.dump(qa_pairs, f, ensure_ascii=False, indent=4)
