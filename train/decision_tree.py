from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np
from numpy.typing import ArrayLike
import train.save_model


class DecisionTree:

    @staticmethod
    def get_criteria():
        return ['gini', 'entropy']

    def __init__(self):
        self.models = []
        for criterion in DecisionTree.get_criteria():
            self.models.append(tree.DecisionTreeClassifier(criterion=criterion))

    def train(self, x_train, x_test, y_train, y_test) -> ArrayLike:
        best_model = None

        for i, clf in enumerate(self.models):
            clf.fit(x_train, y_train)
            predicted = clf.predict(x_test)
            accuracy = accuracy_score(y_test, predicted)
            desc = "Model:{0}, Criterion:{1}, Accuracy:{2}".format("DecisionTreeClassifier",
                                                                  DecisionTree.get_criteria()[i],
                                                                  accuracy)
            print(desc)

            if best_model is None:
                best_model = [clf, accuracy, desc]
            elif accuracy > float(best_model[1]):
                best_model = [clf, accuracy, desc]

        print("Best Model: {0}".format(best_model))
        return best_model
