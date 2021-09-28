class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')


class ManagerRole():
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours')

class SecretaryRole():
    def work(self, hours):
        print(f'{self.name} expands {hours} hours doing office paperworks')

class SalesRole():
    def work(self, hours):
        print(f'{self.name} expands {hours} hours on the phone')

class FactoryRole():
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')