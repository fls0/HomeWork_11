from collections import UserDict
from datetime import datetime, date, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday

    def add_phone(self):
        pass

    def delete_phone(self):
        pass

    def change_phone(self):
        pass

    def days_to_birthday(self):
        if self.birthday:
            birthday = '-'.split()
            d_now = datetime.now()
            br_date = date(day=birthday[0], month=birthday[1], year=d_now.year)
            result = timedelta(br_date - d_now)
            return f'{result.days} days to birthday'


class Field:
    def __init__(self, some_value):
        self.value = some_value


class Name(Field):
    @property
    def value(self):
        return self.some_value
    
    @value.setter
    def value(self, value):
        self.some_value = value


class Phone(Field):
    @property
    def phone_number(self):
        return self.some_value
    
    @phone_number.setter
    def phone_number(self, number): # для перевірки в візьмемо український номер
        flag = True
        for i in number:
            if i.isdigit() or i in '+':
                continue
            else:
                flag = False
                return f'Wrong number'
        if flag:
            if number.startswith('+38') and len(number) == 13:
                self.some_value = number
            elif len(number) == 10:
                self.some_value = number
        else:
            return f'Wrong number'
        
             


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    birthday = '19-02-1999'
    rec = Record(name, phone, birthday)
    maxx = Record('Max','0994690051','19-02-1999')
    rec.days_to_birthday
    maxx.days_to_birthday
