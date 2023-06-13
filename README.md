# prerequisite_QnA

## dataset
#### DSA_LabeledFile, ML_LabeledFile
These are original dataset from http://moocdata.cn/data/prerequisite-relation
#### prepare_data.py
Extract prerequisite relations from dataset, and make CSV file
``` python
if label == '1-':
    concept, prerequisite = concept1, concept2
elif label == '-1':
    concept, prerequisite = concept2, concept1
else:
    # If label is '-', ignore
    continue
```
> #### DSA_prerequisite.csv, ML_prerequisite.csv
> #### prerequisite.csv
> Concatenation of DSA_prerequisite.csv and ML_prerequisite.csv
#### dataset_generate.py
Create dataset as jsonl file, based on prerequisite.csv (for all concepts in prerequisite.csv)
#### validation_generate.py
Create dataset as jsonl file, based on prerequisite.csv (for random 250 concepts only)
```jsonl
{"prompt": "\n[context:agglomerative clustering]\nQ: What field of study should be my first step to know agglomerative clustering?\nA:", "completion": " The primary requirement for understanding agglomerative clustering is an understanding of k means.\n"}
```
> #### QnA_dataset.jsonl
> #### validation_dataset.jsonl

## evaluation
#### question_generation.py
Create questions about random 50 concepts for evaluation in this format:
```python
f'\n[context:{concept}]\nQ: What should I study first to understand {concept}?'
```
> #### questions.txt
> #### query.py
> For extracting query concept from generated questions
#### baseline.py
Using generated questions, get response of baseline model
> baseline_eval.json
#### evaluation.py
Using generated questions, get response of fine-tuned model
Especially the questions contain context field as well
> eval.json
#### evaluation2.py
Using generated questions, get response of fine-tuned model
> eval2.json
#### evaluate.py
Calculate precision, recall, f score

## QnAbot.py
Chatbot which can interactively give question and get response
```shell
export OPENAI_API_KEY="your key"
```
You should get API key from openAI to use baseline.py, evaluation.py, QnAbot.py

## finetuning.ipynb
Fine-tuning code
