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
  ![移动端界面](https://github.com/WxxShirley/FDU_Courses_QA/blob/master/imgs/前端预期效果.jpg.png)
