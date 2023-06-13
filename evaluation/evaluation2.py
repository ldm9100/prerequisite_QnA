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
    
    # Remove the context part
    start = q_line.find('Q: ')  # Finds the start of the question tag and adds 3 to get to the start of the question
    question = q_line[start:]  # Appends the question without the 'Q: ' tag
    questions.append(question)  # If there's no context tag, it appends the line as is

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

with open('eval3.json', 'w') as f:
    json.dump(qa_pairs, f, ensure_ascii=False, indent=4)
