import csv
from collections import defaultdict

# Path of the dataset file
dataset_filepath = 'ML_LabeledFile'        
# Path of the output CSV file
csv_filepath = 'ML_prerequisite.csv'       

# Set context
context = 'machine learning'    

# Set the header for the CSV file
header = ['concept', 'prerequisites', 'context']

# Create a dictionary to store prerequisites for each concept
prerequisite_dict = defaultdict(list)

# Open the dataset file
with open(dataset_filepath, 'r') as dataset_file:
    for line in dataset_file:
        # Split each line by space
        concept1, concept2, label = line.strip().split('    ')

        # Set concept and prerequisite based on the label
        if label == '1-':
            concept, prerequisite = concept1, concept2
        elif label == '-1':
            concept, prerequisite = concept2, concept1
        else:
            # If label is '-', ignore
            continue

        # Add the prerequisite to the list of prerequisites for the concept
        prerequisite_dict[concept].append(prerequisite)

# Open the CSV file
with open(csv_filepath, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()

    # Write to the CSV file
    for concept, prerequisites in prerequisite_dict.items():
        writer.writerow({'concept': concept, 'prerequisites': ', '.join(prerequisites), 'context': context})
