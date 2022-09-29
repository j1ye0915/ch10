class PayrollDeduction:
    
    def __init__(self, description, date, chargeAmt, empID):
        self.__description= description
        self.__date= date
        self.__chargeAmt= chargeAmt
        self.__empID= empID

    def get_Description(self):
        return self.__description
    
    def get_Date(self):
        return self.__date
    
    def get_chargeAmt(self):
        return self.__chargeAmt
    
    def get_EmployeeID(self):
        return self.__empID