from datetime import datetime, timedelta
from collections import UserDict


class Birthday:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


class Record:
    def __init__(self, name, phone, birthday=None):
        self.data = {"name": name, "phone": phone, "birthday": birthday}

    def add_birthday(self, day, month, year):
        self.data["birthday"] = Birthday(day, month, year)

    def __str__(self):
        return f"{self.data['name']} - {self.data['phone']} - {self.data['birthday']}"


class AddressBook(UserDict):
    def add_contact(self, name, phone, birthday=None):
        self.data[name] = Record(name, phone, birthday)

    def change_contact(self, name, phone, birthday=None):
        if name in self.data:
            contact = self.data[name]
            contact.data['phone'] = phone
            if birthday:
                contact.add_birthday(*birthday)
            return "Contact changed."
        return f"Not changed, no user {name}"

    def get_contact_phone(self, name):
        if name in self.data:
            return self.data[name].data['phone']
        return "No such user."

    def get_birthday(self, name):
        if name in self.data:
            birthday = self.data[name].data['birthday']
            return str(birthday) if birthday else f"{name} doesn't have a birthday set."
        return "No such user."

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        next_week = datetime.now() + timedelta(days=7)

        for contact in self.data.values():
            birthday = contact.data['birthday']
            if birthday and (birthday.month == next_week.month) and (birthday.day >= next_week.day):
                upcoming_birthdays.append(contact)

        return upcoming_birthdays


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Incorrect format. Please check your input."
        except KeyError:
            return "No such name found."
        except IndexError:
            return "No input found."
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            name, phone, *birthday = args
            birthday = birthday if birthday else None
            book.add_contact(name, phone, birthday)
            print("Contact added.")
        elif command == "change":
            name, phone, *birthday = args
            birthday = birthday if birthday else None
            print(book.change_contact(name, phone, birthday))
        elif command == "show":
            name = args[0]
            print(book.get_contact_phone(name))
        elif command == "add-birthday":
            name, day, month, year = args
            book.change_contact(name, None, (int(day), int(month), int(year)))
            print("Birthday added.")
        elif command == "show-birthday":
            name = args[0]
            print(book.get_birthday(name))
        elif command == "birthdays":
            birthdays = book.get_upcoming_birthdays()
            if birthdays:
                print("Upcoming birthdays:")
                for contact in birthdays:
                    print(f"{contact.data['name']} - {contact.data['birthday']}")
            else:
                print("No upcoming birthdays in the next week.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
