import re

# Open the file
with open('questions.txt', 'r') as file:
    lines = file.readlines()

# Initialize the list for storing contexts
contexts = []

# Define the pattern to match the context
pattern = r'\[context:(.*?)\]'

# Iterate over the lines in the file
for line in lines:
    # Use the regex search function to find the pattern
    match = re.search(pattern, line)
    
    # If a match was found
    if match:
        # Append the match (without the [context:] part) to the list of contexts
        contexts.append(match.group(1))

# Print the contexts
print(contexts)
