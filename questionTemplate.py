from query import Query
import re
import os
from snownlp import sentiment 

questions = {
    0:"nm 给分", # 课程给分情况
    1:"rr 课程", # 某位老师开设的课程
    2:"nm 类型", # 某门课的类型
    3:"rr sst 课程",    # 某位老师开设的某种类型的课程
    4:"ut 课程", # 某个学院开设了什么课程
    5:"ut sst 课程", #某个学院开设的某种类型的课程
    6:"rr rr 课程",# 教师a与教师b共同上的课
    7:"rr 课程数量",# 某位老师的授课数量
    8:"ut sst 给分好课程", #某个学院开设的给分好的课程
    9:"sst 给分好的课", # 某个类型里给分不错的课
}

# Load the pretrained sentiment classification model

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'sentiment.marshal')
sentiment.load(data_path)

class QuestionTemplate():
    def __init__(self):
        self.q_template_dict = {
            0:self.get_course_rating,
            1:self.get_teacher_courses,
            2:self.get_course_type,
            3:self.get_teacher_type_courses,
            4:self.get_school_courses,
            5:self.get_school_type_courses,
            6:self.get_course_of_2_teacher,
            7:self.get_teacher_course_num,
            8:self.get_school_good_courses,
            9:self.get_type_good_courses,
        }

        self.graph = Query()
    
    def get_question_answer(self,question,template):
        
        assert len(str(template).strip().split("\t"))==2
        template_id, template_str = int(str(template).strip().split("\t")[0]) , str(template).strip().split('\t')[1]
        self.template_id = template_id
        self.template_str2list = str(template_str).split()

        question_word, question_flag = [] , []

        for one in question:
            word, flag = one.split("/")
            question_word.append(str(word).strip())
            question_flag.append(str(flag).strip())
        
        assert len(question_word) == len(question_flag)

        self.question_word = question_word
        self.question_flag = question_flag 
        self.raw_question = question
        
       
        answer = self.q_template_dict[template_id]()

        return answer
    
    # Helper Functions 
    #   Given a type name, return the corresponding word which is tagged as that type
    def get_name(self,type_str):
        
        count = self.question_flag.count(type_str)
        if count == 1:
           index = self.question_flag.index(type_str)
           return self.question_word[index]
        else :
            results = []
            for i,flag in enumerate(self.question_flag):
                if flag == str(type_str):
                    results.append(self.question_word[i])
            return results

    # Question 0 - 课程给分
    def get_course_rating(self):
        course_title = self.get_name("nm")
        sql = f"match (c:Course)-[]->() where c.title='{course_title}' return c.rating"
        answer = self.graph.run(sql)[0]

        res = course_title + "评价情况为" + str(answer) +  "~"
        return res
    

    # Question 1 - 某位老师教的课
    def get_teacher_courses(self):
        teacher = self.get_name("rr")
        sql = f"match(t:Teacher)-[]->(c:Course) where t.name = '{teacher}' return c.title"
        ans_list = self.graph.run(sql)
        ans = "、".join(ans_list)

        res = teacher + "教授的课程有：" + ans + "~"
        return res
    
    # Question 2 - 某门课的类型
    def get_course_type(self):
        course_title = self.get_name("nm")
        sql = f"match(c:Course)-[]->(ct:Course_Type) where c.title = '{course_title}' return ct.name"

        answer = self.graph.run(sql)[0]
        res = course_title + "这门课的类型为" + answer + "~"
        return res

    
    # Question 3 - 某位老师开设的某种类型的课程
    def get_teacher_type_courses(self):
        course_type = self.get_name("sst")
        teacher_name = self.get_name("rr")
        sql = f"match(t:Teacher)-[]->(c:Course) where t.name = '{teacher_name}' return c.title"
        anss = self.graph.run(sql)
        
        results = []
        for course in anss:
            sql = f"match(c:Course)-[]->(ct:Course_Type) where c.title = '{course}' return ct.name"
            type_ = self.graph.run(sql)[0]
            if type_ == course_type:
                results.append(course)
        re_ = " ".join(results)
        res = teacher_name + "开设的" + course_type + "的课程有: " + re_ + "~"

        return res
    
    
    # Question 4 -  某个院系开设的课程
    def get_school_courses(self):
        school = self.get_name("ut")
        sql = f"match(s:School)-[]->(c:Course) where s.name='{school}' return c.title"

        ans = self.graph.run(sql)
       
        anss = "、".join(ans)

        res = school + "开设的课程有: " + anss + "~"
        return res 

    
    # Question 5 - 某个院系开设的某种类型的课
    def get_school_type_courses(self):
        school = self.get_name("ut")
        course_type = self.get_name("sst")
        sql = f"match(s:School)-[]->(c:Course) where s.name='{school}' return c.title"
        ans = self.graph.run(sql)
       
        
        results = []
        for title in ans :
            sql = f"match(c:Course)-[]->(ct:Course_Type) where c.title = '{title}' return ct.name"
            type_ = self.graph.run(sql)[0]
            if type_ == course_type :
                results.append(title)
        
        result = "、".join(results)

        res = school + "开设的" + course_type + "类型的课程有" + result + "等～"
        return res
    

    # Question 6 - 教师a与教师b共同上的课
    def get_course_of_2_teacher(self):
        teachers = self.get_name("rr")
        print("in")
        courses = {}
    
        for i,teacher in enumerate(teachers):
            sql = f"match(t:Teacher)-[]->(c:Course) where t.name = '{teacher}' return c.title"
            ans = self.graph.run(sql)
            courses[i] = ans

        res_list = list(set(courses[0]).intersection(set(courses[1])))
        answer = "、".join(res_list)

        res = teachers[0] + "和" + teachers[1] + "共同上的课是" + answer + "~"
        return res 
    

    # Question 7 - 某位教师的授课数量
    def get_teacher_course_num(self):
        teacher = self.get_name("rr")

        sql = f"match(t:Teacher)-[] -> (c:Course) where t.name = '{teacher}' return c.title"

        ans = self.graph.run(sql)
        num = len(ans)
        
        res = teacher + "授课数量为" + str(num) + "~"
        return res 


    # Question 8 - 某个学院开设的给分好的课程

    def get_school_good_courses(self):
        school = self.get_name("ut")

        course_type = self.get_name("sst")

        sql = f"match(s:School)-[] -> (c:Course) where s.name = '{school}' return c.title"
        courses = self.graph.run(sql)
        
        results = []

        for course in courses:
            sql = f"match(c:Course)-[] ->(ce:Course_Type) where c.title = '{course}' return ce.name"
            type_ = self.graph.run(sql)[0]
            if type_ == course_type:
                sql = f"match (c:Course)-[]->() where c.title='{course}' return c.rating"
                rating = self.graph.run(sql)[0]
                score = sentiment.classify(rating)
                if score >= 0.4:
                    print(course,score)
                    results.append(course)
        
        if len(results) == 0:
            return "该院系没有对应的课程"
        else :
            res = "、".join(results)
        
        ret = school + "开设的" + "评价不错的" + course_type + "有: " + res + "等～"
        return ret

    # Question 9 - 某个类型的课程中评价不错的课
    def get_type_good_courses(self):

        #print("in")
        course_type = self.get_name("sst")
        sql = f"match(c:Course) return c.title"
        ans = self.graph.run(sql)
        
        results = []
        for course in ans :
            sql = f"match(c:Course)-[] ->(ce:Course_Type) where c.title = '{course}' return ce.name"
            type_ = self.graph.run(sql)[0]

            if type_ == course_type :
                sql = f"match(c:Course)-[]->() where c.title = '{course}' return c.rating"
                rating = self.graph.run(sql)[0]
                score = sentiment.classify(rating)
                if score >= 0.4:
                    print(course,score)
                    results.append(course)

        if len(results)>0:
            res_ = "、".join(results)
        else :
            return "该类型下没有对应的课程"


        res = course_type + "评价不错的课程有: " + res_ + "等～"
        return res 





