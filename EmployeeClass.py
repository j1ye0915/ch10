class Employee:

    def __init__(self,name,IdNum,department,jobTitle,MonSalary):
        self.___name = name
        self.__IdNum = IdNum
        self.__department = department
        self.__jobTitle = jobTitle
        self.__MonSalary = MonSalary

    def get_Name(self):
        return self.___name

    def get_IdNum(self):
        return self.__IdNum

    def get_department(self):
        return self.__department

    def get_jobTitle(self):
        return self.__jobTitle
        
    def get_MonSalary(self):
        return self.__MonSalary

    