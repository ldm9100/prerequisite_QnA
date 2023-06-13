import pandas as pd
import numpy as np

df = pd.read_csv('../dataset/prerequisite.csv')

def generate_questions(df, num_questions):
    random_concepts = df['concept'].sample(n=num_questions)
    
    questions = []
    
    for concept in random_concepts:
        question = f'\n[context:{concept}]\nQ: What should I study first to understand {concept}?'
        questions.append(question)
    
    return questions

questions = generate_questions(df, 50)

with open('questions.txt', 'w') as f:
    for i, question in enumerate(questions):
        f.write(f'{question}\n')
