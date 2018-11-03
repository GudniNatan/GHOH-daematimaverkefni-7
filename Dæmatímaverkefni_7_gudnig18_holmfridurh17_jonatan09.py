class Person(object):
    def __init__(self, name="", userName="", ssn=0):
        self.__name = name
        self.__userName = userName
        self.__ssn = ssn

    def getName(self):
        return self.__name

    def getUserName(self):
        return self.__userName

    def getSSN(self):
        return self.__ssn


class Student(Person):
    def __init__(self, name='', userName='', ssn=0, department=""):
        super().__init__(name=name, userName=userName, ssn=ssn)
        self.__department = department

    def getDepartment(self):
        return self.__department


class Professor(Person):
    def __init__(self, name='', userName='', ssn=0, position=""):
        super().__init__(name=name, userName=userName, ssn=ssn)
        self.__position = position

    def getPosition(self):
        return self.__position


class Course(object):
    def __init__(self, students, professor, name=""):
        self.__students = students
        self.__professor = professor
        self.__name = name

    def getName(self):
        return self.__name

    def getStudents(self):
        return self.__students

    def getProfessor(self):
        return self.__professor
