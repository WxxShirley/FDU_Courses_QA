from py2neo import Graph,Node,Relationship,NodeMatcher


class Query():
    def __init__(self):
        self.graph = Graph("http://localhost:7474",username="neo4j",password="622868")
    
    def run(self,sql):
        result = []
        find_rela = self.graph.run(sql)

        for i in find_rela:
            result.append(i.items()[0][1])
        
        return result


if __name__ == "__main__":
    
    sql = Query()
    courses = sql.run("match(c:Course) return c.title") # nm
    teachers = sql.run("match(t:Teacher) return t.name") # rr
    schools = sql.run("match(s:School) return s.name") # ut
    course_types = sql.run("match(ce:Course_Type) return ce.name") # sst

    course_tags , teacher_tags, school_tags , course_tags = [], [] ,[] , []
    
    for course in courses :
        content = course + " 15 " + "nm"
        course_tags.append(content)
    
    for teacher in teachers :
        content = teacher + " 15 " +"rr"
        teacher_tags.append(content)
    
    for school in schools :
        content = school + " 15 " + "ut"
        school_tags.append(content)
    
    for course_type in course_types:
        content = course_type + " 15 " + "sst"
        course_tags.append(content)
    
    contents = course_tags + teacher_tags + school_tags + course_tags 

   
    file_write_obj = open("dict.txt",'w')
    for c in contents:
        file_write_obj.writelines(c)
        file_write_obj.write('\n')
   