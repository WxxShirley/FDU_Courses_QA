from snownlp import sentiment
from snownlp import SnowNLP
import os

if __name__ == "__main__":
    #sentiment.train('neg.txt','pos.txt')
    #sentiment.save('sentiment.marshal')
    #print(sentiment.classify('老师人特别好，课程内容比较轻松'))
    
    #data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'sentiment.marshal')
    #sentiment.load(data_path)
    #print(sentiment.classify('老师人特别好，课程内容比较轻松'))
    s = SnowNLP(u'老师人特别好，课程内容比较轻松')
    print(s.sentiments)