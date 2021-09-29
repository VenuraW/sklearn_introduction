from sklearn.model_selection import GridSearchCV

def print_score(name, classifier, dataset):
    classifier.fit(dataset[0], dataset[2])
    score = classifier.score(dataset[1], dataset[3])
    print("{} score: {:.2f}%".format(name, score*100))

def print_tuned_score(parameters, classifier, dataset):
    grid_search = GridSearchCV(estimator=classifier,
                               param_grid=parameters,
                               scoring='accuracy',
                               cv=10)
    grid_search.fit(dataset[0], dataset[2])
    classifier = grid_search.best_estimator_
    score = classifier.score(dataset[1], dataset[3])
    print("Tuned parameters score: {:.2f}%".format(score * 100))