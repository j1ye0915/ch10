import EmployeeClass as e
import PayrollDeductionClass as pd

employee = e.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

deduction1= pd.PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
deduction2= pd.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
deduction3= pd.PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
deduction4= pd.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
deduction5= pd.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

print("*** Employee Pay ***")
print("Name:", employee.get_Name())
print("ID Number:", employee.get_IdNum())
print("Department:", employee.get_department())
print("Gross Pay: $", float(employee.get_MonSalary()), sep='')
print("Net Pay: $", employee.get_MonSalary()-deduction2.get_chargeAmt()-deduction4.get_chargeAmt()-deduction5.get_chargeAmt(), sep='')