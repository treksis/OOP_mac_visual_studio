# The PayrollSystem implements a .calculate_payroll() method that takes a collection of employees and prints their id, 
# name and check amount using .calcualte_payroll() method exposed on each employee object

class PayrollSystem:
    def calculate_payroll(self, employees): # employees = []
        print("Calculating payroll")
        print("===================")

        for employee in employees:
            print(f"payroll for: {employee.id} - {employee.name}")
            print(f"- check amount {employee.calculate_payroll()}")
            if employee.address:
                print('-sent to:')
                print(employee.address)
            print('')


# What it is saying that every Employee must have an id assigned as well as a name
# The HR system requires that every Employee processed must provide a .calculate_payroll() interface that 
# returns the weekly salary for the employee

#from abc import ABC, abstractmethod

class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission
    
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


