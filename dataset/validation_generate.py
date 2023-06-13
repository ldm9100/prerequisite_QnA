import pandas as pd
import random
import json

# Yield successive n-sized chunks from lst.
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Load CSV into DataFrame
df = pd.read_csv('prerequisite.csv')

# Define your templates
prompt_templates = [
   "\n[context:{concept}]\nQ: Which topic should I delve into first to comprehend {concept}?\nA:",
   "\n[context:{concept}]\nQ: What is the initial area of study I need to grasp {concept}?\nA:",
   "\n[context:{concept}]\nQ: What is the foundational knowledge required to understand {concept}?\nA:",
   "\n[context:{concept}]\nQ: What subject must I learn first to get the gist of {concept}?\nA:",
   "\n[context:{concept}]\nQ: What is the preliminary learning necessary to master {concept}?\nA:",
   "\n[context:{concept}]\nQ: What's the first area of knowledge I need to acquire to comprehend {concept}?\nA:",
   "\n[context:{concept}]\nQ: To understand {concept}, where should I start my studies?\nA:",
   "\n[context:{concept}]\nQ: What is the starting point of learning to understand {concept}?\nA:",
   "\n[context:{concept}]\nQ: Which course should I take on first to understand {concept}?\nA:",
   "\n[context:{concept}]\nQ: What do I need to study initially to get a clear understanding of {concept}?\nA:",
   "\n[context:{concept}]\nQ: What field of study should be my first step to know {concept}?\nA:",
   "\n[context:{concept}]\nQ: Where should my educational journey start to grasp {concept}?\nA:",
   "\n[context:{concept}]\nQ: What is the first topic I should tackle to comprehend {concept}?\nA:",
   "\n[context:{concept}]\nQ: To get a handle on {concept}, what should be my first area of study?\nA:",
   "\n[context:{concept}]\nQ: What's the initial subject matter I need to study to understand {concept}?\nA:",
   "\n[context:{concept}]\nQ: What should be my starting point in learning about {concept}?\nA:",
   "\n[context:{concept}]\nQ: What's the primary study requirement for understanding {concept}?\nA:",
   "\n[context:{concept}]\nQ: Which subject is fundamental to get an understanding of {concept}?\nA:",
   "\n[context:{concept}]\nQ: What's the first academic step I need to take to comprehend {concept}?\nA:",
   "\n[context:{concept}]\nQ: Which study material should I start with to understand {concept}?\nA:"
]

completion_templates = [
    " To grasp the {concept}, it's imperative you first delve into {prerequisite}.\n",
    " Begin with studying {prerequisite}, it's foundational for understanding {concept}.\n",
    " Your comprehension of {concept} will significantly benefit from an initial study of {prerequisite}.\n",
    " Kick off your learning journey with {prerequisite}, it's crucial for understanding {concept}.\n",
    " The key to unlocking {concept} is to start with studying {prerequisite}.\n",
    " Your first step towards understanding {concept} should be mastering {prerequisite}.\n",
    " Start your educational journey with {prerequisite}, it will pave the way to understanding {concept}.\n",
    " To get to the heart of {concept}, your studies should commence with {prerequisite}.\n",
    " {prerequisite} is the initial pillar of knowledge you should study to comprehend {concept}.\n",
    " To get a clear understanding of {concept}, begin by studying {prerequisite}.\n",
    " To unravel the complexities of {concept}, immerse yourself in {prerequisite} first.\n",
    " Understanding {concept} starts with a thorough study of {prerequisite}.\n",
    " Begin your academic venture into {concept} by focusing on {prerequisite}.\n",
    " Mastering {concept} involves starting your studies with {prerequisite}.\n",
    " Your understanding of {concept} hinges upon a solid foundation in {prerequisite}.\n",
    " The best starting point for learning about {concept} is studying {prerequisite}.\n",
    " The primary requirement for understanding {concept} is an understanding of {prerequisite}.\n",
    " To truly grasp {concept}, it's important to first study {prerequisite}.\n",
    " Your first academic step to comprehending {concept} should be studying {prerequisite}.\n",
    " Initiate your exploration of {concept} with a deep dive into {prerequisite}.\n"
]

# Number of pairs to generate
target = 250

# Open a new JSONL file
with open('validation_dataset.jsonl', 'w') as f:
    # Generate pairs until the target is reached
    while target > 0:
        # Randomly select a row from the DataFrame
        row = df.sample(1).iloc[0]

        concept = row['concept']
        context = row['context']
        prerequisites = row['prerequisites'].split(", ")

        # Select one or two random prerequisites
        prereqs_to_use = random.sample(prerequisites, min(len(prerequisites), random.choice([1, 2])))

        # Select a random prompt and completion template
        prompt_template = random.choice(prompt_templates)
        completion_template = random.choice(completion_templates)

        # Join the prerequisites with a comma and space if there are more than one
        prereq_to_use = ", ".join(prereqs_to_use)

        # Populate the templates
        populated_prompt = prompt_template.format(concept=concept)
        populated_completion = completion_template.format(concept=concept, prerequisite=prereq_to_use)

        # Write to JSONL file
        f.write(json.dumps({"prompt": populated_prompt, "completion": populated_completion}) + '\n')

        # If we've hit the target number of pairs, stop writing to the file
        target -= 1