# Importing the libraries
from preprocessing import split_set
from classifier import Classifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

models = []

# Adding Logistic Regression Model
models.append({"name": "Logistic Regression",
               "classifier": LogisticRegression(),
               "params": [{'penalty': ['l2', 'none'], 'solver':['newton-cg', 'lbfgs']},
                          {'penalty': ['l1', 'l2'], 'solver': ['liblinear']}]})

sorted_classifiers = [0] * len(models)

# Training models
for model in models:
    classifier = Classifier(model["name"], model["classifier"], split_set)

    # Training default model and using grid search to find best classifier
    classifier.train_classifier()
    classifier.train_grid_search(model["params"])
    classifier.set_best_classifer()

    # Find position in array to add
    insert_index = 0
    while sorted_classifiers[insert_index] != 0:
        if sorted_classifiers[insert_index].get_best_score() < classifier.get_best_score():
            break
        insert_index += 1

    sorted_classifiers[insert_index:insert_index] = [classifier]

# Printing models by name and score
for i in range(len(models)):
    print("{}. {} Score: {:.2f}%".format(i + 1, sorted_classifiers[i].get_name(), sorted_classifiers[i].get_best_score()*100))