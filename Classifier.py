# load the package

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

import os 
import re
import jieba 
from questions import *
import random

class Question_classify():
    def __init__(self):
        self.train_x, self.train_y = self.load_data()
        self.model = self.train_NB()
    
    def load_data(self):
        train_x = []
        train_y = []
        train = []
        jieba.add_word("给分",tag = "v")
        questions = [q0 ,q1 ,q2 ,q3 ,q4 ,q5 ,q6 ,q7,q8 ,q9]
        #questions = [q1,q2]

        for q in questions:
            label = questions.index(q)
            for line in q:
                word_list = list(jieba.cut(str(line).strip()))
                train_x.append(" ".join(word_list))
                train_y.append(label)
        return train_x,train_y
            
        """
        random.shuffle(train)

        for i in range(len(train)):
            length = len(train[i])
            train_y.append(int(train[i][-1]))
            train_x.append(train[i][:length-1])
        
        return train_x, train_y
        """

    def train_NB(self):
        #print(self.train_x)
        #print(self.train_y)
        X_train, y_train = self.train_x, self.train_y
        self.tv = TfidfVectorizer()

        train_data = self.tv.fit_transform(X_train).toarray()
        clf = MultinomialNB(alpha=0.01)
        #clf = DecisionTreeClassifier(criterion='entropy')
        clf.fit(train_data, y_train)
        
        return clf
    
    def predict(self,question):
        question = [" ".join(list(jieba.cut(question)))]
        test_data = self.tv.transform(question).toarray()
        predict = self.model.predict(test_data)[0]
        return predict
    

if __name__ == "__main__":
    qc = Question_classify()
    print(qc.predict("计算机学院开设的给分好的专业选修"))
    print(qc.predict("通识教育选修中给分不错的课"))
    