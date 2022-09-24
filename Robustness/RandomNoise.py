import numpy as np
from sklearn import metrics

def plus(numbers: list):
    value = 0 
    for number in numbers:
        value += number
    return value


def addNoise(X, scale=0.1):
    print(X)
    return X + np.random.normal(0, scale, X.shape)

def evaluate(model, X_train, y_train, X_test, y_test, values= np.linspace(0, 0.5, 30)):
    accuracy_scores = []
    for value in values: 
        model.fit(addNoise(X_train, value), y_train)
        accuracy_scores.append(metrics.accuracy_score(y_test, model.predict(X_test)))
    return accuracy_scores, values
