class Address:
    def __init__(self, address, apt, state, city, zip_code):
        self.__address = address
        self.__apt = apt
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code

    @property
    def full_address(self):
        return f'{self.__address} {self.__apt}  {self.__city}, {self.__state} {self.__zip_code}'

    @property
    def address(self):
        return f'{self.__address} {self.__apt}'

    @property
    def city(self):
        return f'{self.__city}'

    @property
    def state(self):
        return f'{self.__state}'

    @property
    def zip_code(self):
        return f'{self.__zip_code}'


class Person:
    def __init__(self, first_name, last_name, age, phone, email, address: Address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__work = []
        self.__symptoms = []

    @property
    def name(self):
        return f'{self.__last_name.capitalize()}, {self.__first_name.capitalize()}'

    @property
    def age(self):
        return f'{self.__age}'

    @property
    def phone(self):
        return f'{self.__phone}'

    @property
    def email(self):
        return f'{self.__email}'

    @property
    def where(self):
        return self.__address.full_address

    @property
    def get_address(self):
        return self.__address

    def add_work(self, name, phone, email, work_address) -> dict:
        new_work = {'name': name, 'email': email, 'phone': phone, 'address': work_address}
        self.__work.append(new_work)
        return new_work

    @property
    def list_of_work(self) -> list:
        return self.__work

    def add_symptoms(self, symptoms: dict):

        self.__symptoms = symptoms

    @property
    def symptoms(self):
        return self.__symptoms
