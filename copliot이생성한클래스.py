class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
if __name__ == "__main__":
    # Person 테스트
    p1 = Person(1, "Alice")
    p2 = Person(2, "Bob")
    
    # Manager 테스트
    m1 = Manager(3, "Charlie", "Team Lead")
    m2 = Manager(4, "David", "Project Manager")
    
    # Employee 테스트
    e1 = Employee(5, "Eve", "Python")
    e2 = Employee(6, "Frank", "Java")
    e3 = Employee(7, "Grace", "C++")
    e4 = Employee(8, "Hank", "JavaScript")
    e5 = Employee(9, "Ivy", "Go")
    e6 = Employee(10, "Jack", "Swift")
    
    # 출력 테스트
    p1.printInfo()
    p2.printInfo()
    m1.printInfo()
    m2.printInfo()
    e1.printInfo()
    e2.printInfo()
    e3.printInfo()
    e4.printInfo()
    e5.printInfo()
    e6.printInfo()