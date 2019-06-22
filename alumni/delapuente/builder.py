
class Address:

    def __init__(self, *args):
        ...

class Profile:

    def __init__(self, name, surname, address, picture, social_profile, phone_number, birth_date, local_id_number, email):
        self.name = name
        ...


class ProfileBuilder:

    def __init__(self):
        self._name = None
        self._surname = None

    def name(self, name):
        self._name = name
        return self

    def address(self, postal_address):
        self._postal_address = postal_address
        return self

    def get_profile(self):
        if self._name is None:
            raise ValueError('name is mandatory')
        address = Address(self._postal_address)
        return Profile(self._name, self._surname, address, '', '', '', '', '', '', '', '', '')


salva = ProfileBuilder()\
    .name('Salva')\
    .address('Adrian Pulido')\
    .get_profile()

assert salva.name == 'Salva'