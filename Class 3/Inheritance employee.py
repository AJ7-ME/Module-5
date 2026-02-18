class person ( object ):
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum
    def display(self):
        print(self.name)
        print(self.idnum)
class Employee( person ):
    def __init__(self, name, idnum, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, idnum)
a = Employee('MR CEO', 886012, 999999999999, "CEO")
a.display()