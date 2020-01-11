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
    #res = sql.run("match(c:Course)-[] ->(ce:Course_Type) where c.title = '自然语言处理' return ce.name , c.rating")
    res = sql.run("match(c:Course)  return c.title")
    print(res)