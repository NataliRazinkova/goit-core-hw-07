from datetime import datetime

class Birthday():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def add_birthday(self, birthday):
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
            self.birthday = birthday
        except ValueError:
            print("Incorrect birthday format. Please use YYYY-MM-DD format.")

    def validate_phone(self, phone):
        pass

    def validate_birthday(self, birthday):
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
            return True
        except ValueError:
            return False

record = Record("John Doe", "123-456-7890")
record.add_birthday("1990-05-15")
print(record.birthday)

class AddressBook:
    def __init__(self):
        self.contacts = []

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        next_week = datetime.now() + timedelta(days=7)

        for contact in self.contacts:
            if contact.birthday is not None:
                if contact.birthday.month == next_week.month and contact.birthday.day >= next_week.day:
                    upcoming_birthdays.append(contact)

        return upcoming_birthdays

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "No found"

    return inner
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if args[0] in contacts.keys():
        add_contact(args, contacts)
    else:
        print (f"Not changet, no user {args[0]}")

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name] if name in contacts.keys() else "No such user"

@input_error  
def show_all(args, contacts):
    s=''
    for key in contacts:
        s+=(f"{key:10} : {contacts[key]:10}\n")
    return s

@input_error
def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(args,contacts))
        else:
            print("Invalid command.")

@input_error
def add_birthday(self, birthday):
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
            self.birthday = birthday
        except ValueError:
            print("Incorrect birthday format. Please use YYYY-MM-DD format.")

if __name__ == "__main__":
    main()

