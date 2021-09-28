class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('121 Admin rd.', 'Concord', 'NH', '03301'),
            2: Address('403 Ninja st', 'London', 'NA', '11451'),
            3: Address('56 charlotte rd', 'Kirkland', 'OH', '123123', 'Apt. B-1'),
            4: Address('39 chichi', 'seoul', 'seoul', '12345'),
            5: Address('91 Mountain rocky', 'canada', 'canada', '112312')
        }

    def get_employee_address(self, emplyoee_id):
        address = self._employee_addresses.get(emplyoee_id)
        if not address:
            raise ValueError(emplyoee_id)
        return Address

class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state} {self.zipcode}")
        return '\n'.join(lines)
