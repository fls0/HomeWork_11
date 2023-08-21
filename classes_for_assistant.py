from collections import UserDict
from datetime import datetime, date, timedelta
import dateparser

class Iterator:
    MAX_ITERATIONS = 1

    def __init__(self, n=1):
        self.n = n
        self.current_value = 0
    
    def __next__(self):
        if self.current_value < self.MAX_ITERATIONS:
            self.current_value += 1
            return 
        raise StopIteration

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def __iter__(self, n_records):
        return Iterator(n_records)


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
            self.phone = phone
        if birthday:
            self.birthday = Birthday(birthday)

    def add_phone(self):
        pass

    def delete_phone(self):
        pass

    def change_phone(self):
        pass

    def days_to_birthday(self):
        pass


class Field:
    def __init__(self, some_value):
        self.value = some_value

    @property
    def value(self):
        return self.some_value

    @value.setter
    def value(self, value):
        self.some_value = value


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
    def phone_number(self, number):  # для перевірки в візьмемо український номер
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


class Birthday:
    def __init__(self, value):
        self.value = value

    @property
    def birthday(self):
        return self.value

    @birthday.setter
    def birthday(self, value):
        try:
            date_parce = dateparser.parse(value)
            self.value = date_parce
        except:
            raise f'Wrong birthday date'


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    birthday = '19-02-1999'
    rec = Record(name, phone, birthday)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')
    for i in ab:
        print(i)
