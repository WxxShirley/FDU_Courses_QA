import jieba
import jieba.posseg
import jieba.analyse as anal
import re
from Classifier import Question_classify
from questionTemplate import * 


class Question():
    def __init__(self):
        self.init_config()
    
    def init_config(self):

        # Train the model 
        self.classify_model = Question_classify()

        # Question_Dictionary 
        self.question_mode_dict = questions

        # Create a question teamplate 
        self.questionTemplate = QuestionTemplate()
    
    def process_question(self,question):
        # raw question 
        self.raw_question = str(question).strip()
        
        self.pos_question = self.question_posseg()

        self.question_template_id_str = self.get_question_template()
        
        self.answer = self.query_template()

        return self.answer
    


    def question_posseg(self):
        jieba.load_userdict('dict.txt')
        jieba.add_word("给分",tag = 'v')
        # clean the question
        clean_question = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",self.raw_question)

        self.clean_question = clean_question

        question_seged = jieba.posseg.cut(str(clean_question))
        result = []

        question_word, question_flag = [] , []

        for w in question_seged:
            temp_word = f"{w.word}/{w.flag}"
            result.append(temp_word)

            word,flag = w.word, w.flag
            question_word.append(str(word).strip())
            question_flag.append(str(flag).strip())
        
        assert len(question_word) == len(question_flag)
        
        self.question_word = question_word
        self.question_flag = question_flag


        return result 
    

    def get_question_template(self):
        for item in ['nm','sst','ut','rr']:
            if item in self.question_flag:
                index = self.question_flag.index(item)
                self.question_word[index] = item
                #self.question_flag[index] = item + "ed"
        
        str_question="".join(self.question_word)
        print("抽象问题为:",str_question)

        question_template_num = self.classify_model.predict(str_question)
        print("使用模版编号： ",question_template_num)
        question_template = self.question_mode_dict[question_template_num]
        print("问题模版：",question_template)

        question_template_id_str = str(question_template_num) + "\t" + question_template
        
        return question_template_id_str
    
    def query_template(self):
        try:
            answer = self.questionTemplate.get_question_answer(self.pos_question,self.question_template_id_str)
        except:
            answer = "我也还不知道"
        
        return answer


if __name__ == "__main__":
    que = Question()
    #result = que.process_question("计算机科学技术学院开设给分好的专业必修")
    #result = que.process_question("通识教育选修中给分不错的课")
    #result = que.process_question("陶晓鹏老师上哪些课")
    result = que.process_question("评价不错的七大模块课程")
    #que.raw_question = "自然语言处理给分怎么样"
    #print(que.question_posseg())
    
    print(result)
    #print(que.question_word,que.question_flag)