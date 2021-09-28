from productivity import ProductivitySystem
from hr import PayrollSystem
from contacts import AddressBook

class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Many Poppins',
                'role': 'Manager'
            },
            {
                'id': 2,
               'name': 'John Smith',
               'role': 'secretary'
            }, 
            {
                'id': 3,
                'name': 'Kevin Bacon',
                'role': 'sales'
            }, 
            {
                'id': 4,
                'name': 'Jane Doe',
                'role': 'factory'
            }, 
            {
                'id': 5,
                'name': 'Robin Williams',
                'role': 'secretary'
            }
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_address = AddressBook()

    @property
    def employee(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_address.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)