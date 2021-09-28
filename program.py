import hr
import disgruntled

salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500) # id, name, weekly salary
hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15) #id, name, hourly worked, hourly salary
commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
disgruntled_emplyoee = disgruntled.DisgruntledEmployee(20000, "Anonymous")
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee,
    hourly_employee,
    commission_employee,
    disgruntled_emplyoee
    ])