## course_review 
该目录为预训练文本情感分析模型

* 训练数据在`reviews.csv`下，从公众号“复小七”上爬取的课程评价。
  格式为   [ 评价文本， 对应标记] 

* 训练代码在 sentimentTrain.py 文件下 ，使用SnowNLP训练

* 正负样本文本内容分别在 `pos.txt` 和 `neg.txt` 中

* 正负样本文本内容词云图在 `wordcloud` 目录下

* 模型用途：预训练情感分类器，以筛选用户所需的“评价不错的课程”
