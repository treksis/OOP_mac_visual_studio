import hr
import employees

"""
salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500) # id, name, weekly salary
hourly_employee = employees.HourlyEmployee(2, 'Jane Doe', 40, 15) #id, name, hourly worked, hourly salary
commission_employee = employees.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
#disgruntled_emplyoee = disgruntled.DisgruntledEmployee(20000, "Anonymous")
payroll_system = employees.PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee,
    hourly_employee,
    commission_employee,
    #disgruntled_emplyoee
    ])
"""

import productivity

manager = employees.Manager(1, 'Many poppins', 3000)
secretary = employees.Secretary(2, 'John Smith', 1500)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary
]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)

