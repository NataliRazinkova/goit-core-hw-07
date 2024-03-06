from datetime import datetime, timedelta

class Birthday:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def add_birthday(self, day, month, year):
        self.birthday = Birthday(day, month, year)

class AddressBook:
    def __init__(self):
        self.data = []

    def add_contact(self, name, phone, birthday=None):
        self.data.append(Record(name, phone, birthday))

    def change_contact(self, name, phone, birthday=None):
        for contact in self.data:
            if contact.name == name:
                contact.phone = phone
                if birthday:
                    contact.add_birthday(*birthday)
                return "Contact changed."
        return f"Not changed, no user {name}"

    def get_contact_phone(self, name):
        for contact in self.data:
            if contact.name == name:
                return contact.phone
        return "No such user."

    def get_birthday(self, name):
        for contact in self.data:
            if contact.name == name:
                if contact.birthday:
                    return f"{contact.name}'s birthday is on {contact.birthday.day}.{contact.birthday.month}.{contact.birthday.year}"
                else:
                    return f"{contact.name} doesn't have a birthday set."
        return "No such user."

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        next_week = datetime.now() + timedelta(days=7)

        for contact in self.data:
            if contact.birthday is not None:
                if (contact.birthday.month == next_week.month and
                        contact.birthday.day >= next_week.day):
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
            book.change_contact(name, None, (day, month, year))
            print("Birthday added.")
        elif command == "show-birthday":
            name = args[0]
            print(book.get_birthday(name))
        elif command == "birthdays":
            birthdays = book.get_upcoming_birthdays()
            if birthdays:
                print("Upcoming birthdays:")
                for contact in birthdays:
                    print(f"{contact.name} - {contact.birthday.day}.{contact.birthday.month}.{contact.birthday.year}")
            else:
                print("No upcoming birthdays in the next week.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
