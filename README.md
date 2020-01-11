# FDU_Courses_QA
复旦选课问答系统，自然语言处理课程pj

## 环境

* python 3.7
* jieba
* snownlp
* sklearn
* pyneo
* neo4j桌面端

## 运行

* 安装*neo4j*图数据库，将 */data* 目录下的所有*.csv* 文件导入图数据库中，执行的指令内容在 */Graph_database_Commands* 下。
* 运行 *question_process* 文件，如改变不同的问题，修改main函数即可 

* 结果示例 
   ![结果示例](https://github.com/WxxShirley/FDU_Courses_QA/blob/master/imgs/运行结果示例.png)
   ![结果示例2](https://github.com/WxxShirley/FDU_Courses_QA/blob/master/imgs/运行结果示例2.png)
 
 
## 功能

* 支持十类复旦选课相关的问题
  * 某门课程的给分情况
  * 某位老师教的课程名
  * 某位老师的教课数量
  * 某门课程的类型
  * 某位老师教的某种类型的课程
  * 某个学院开设的课程
  * 某个学院开设的某种类型的课程
  * 某个学院开设的评价不错的某种类型的课程 
  * 两位老师一起教的课程
  * 某个类型里评价不错的课程

* 初步构思的移动端界面
 
   ![移动端界面](https://github.com/WxxShirley/FDU_Courses_QA/blob/master/imgs/移动端效果图.png)

* 拓展
  * 数据规模较小，可从教务网站上爬取更多课程信息，导入图数据库中
  * 提供的查询累问题规模略小，可以在 *questions.py* 里增加新的问题并训练，在 *questionTemplate.py* 里增加该问题对应的查询思路即可

## 实现思路

![项目工作流程](https://github.com/WxxShirley/FDU_Courses_QA/blob/master/imgs/项目工作流程.png)
* 预训练模型
  * 基于朴素贝叶斯模型的问题分类器，识别用户提问对应哪一类 （数据在 'question.py' 文件下）
  * 基于SnowNLP的情感分析，为新的课程评价计算情感得分，以筛选出“评价不错”的课程 （数据在 /reviews 子目录下，爬取公众号“复小七”的课程评价数据。
    训练好的模型为 sentiment.marshal.3)

