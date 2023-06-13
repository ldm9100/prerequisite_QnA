import csv
import json

with open('../dataset/prerequisite.csv', 'r') as f:
    rdr = csv.reader(f)
    prerequisite = {}
    for line in rdr:
        key = line.pop(0)
        prerequisite[key] = line[0].split(", ")
    f.close()

with open('./eval2.json', 'r') as json_file:
    json_data = json.load(json_file)
    answer_list = []
    for instance in json_data:
        answer_list.append(instance["answer"])

baseline_query = ['linear inequality', 'traveling salesman problem', 'true negatives', 'minimum dist', 'balanced search', 'mst verification', 'square distances', 'recommender system', 'eulerian cycle', 'generalized linear models', 'big omega', 'normalized representation', 'regularized logistic regression', 'gradient checking', 'red black tree', 'polynomial algorithm', 'agglomerative clustering', 'principle components', 'neural network', 'shortest path algorithm', 'edmonds-karp algorithm', 'online learning', 'connected component', 'model selection', 'binary classification', 'precision recall curve', 'randomized quick sort', 'evaluation metrics', 'connected graph', 'search tree', 'o notation', 'asymptotic analysis', 'binary search tree', 'residual graph', 'maximum likelihood estimate', 'probabilistic model', 'mst algorithm', 'latent dirichlet allocation', 'union find', 'binary heap', 'linear function', 'np-complete problem', 'search algorithm', 'greedy algorithm', 'merge sort', 'suffix trie', 'suffix tree', 'spanning tree algorithm', 'nonlinear hypotheses', 'positive training example']

def compute_recall():
    n_correct_answers = 0
    for query in baseline_query:
        n_correct_answers += len(prerequisite[query])
    n_correct_prediction = 0
    for i in range(len(answer_list)):
        correct_answers = prerequisite[baseline_query[i]]
        for answer in correct_answers:
            if answer in answer_list[i]:
                n_correct_prediction += 1
    recall = n_correct_prediction/n_correct_answers
    print(n_correct_prediction)
    print("recall: ", recall)
    return recall

def compute_precision():
    n_correct_prediction = 0
    for i in range(len(answer_list)):
        correct_answers = prerequisite[baseline_query[i]]
        for answer in correct_answers:
            if answer in answer_list[i]:
                n_correct_prediction += 1
    precision = n_correct_prediction/88        # 84 for fine-tuned model / 126 for baseline mode / 88 for general quesition
    print("precision: ", precision)
    return precision
        
recall = compute_recall()
precision = compute_precision()
beta = 0.5
if precision + recall == 0:
    print("f score: 0")
else:
    f_score = (1+beta*beta) * (precision * recall) / (beta*beta*precision + recall)
    print("f score: ", f_score)