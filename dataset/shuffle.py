import json
import random

# Read the JSONL file.
with open('validation_dataset.jsonl', 'r') as f:
    data = [json.loads(line) for line in f]

# Randomly shuffle the order of the data.
random.shuffle(data)

# Save the randomly shuffled data to a new file.
with open('validation_dataset.jsonl', 'w') as f:
    for item in data:
        f.write(json.dumps(item) + '\n')
