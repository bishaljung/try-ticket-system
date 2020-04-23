# here i am going to create the ticket system using class and object for learning purpose.
import pickle
class passenger:
    # The _ _init_ _ method initializes the attributes of class passenger.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # The set_name,phone,email  method sets the name, phone and email attribute.
    def set_name(self, name):
        self.__name = name
    def set_phone(self, phone):
        self.__phone = phone
    def set_email(self, email):
        self.__email = email

    # The get_name, get_phone,get_email method returns the name,phone and email attribute.
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email

    # The _ _str_ _ method returns the object's state as a String.
    def __str__(self):
        return "Name: " + self.__name + \
               "\nPhone: " + self.__phone + \
               "\nEmail: " + self.__email


'''class vehicle:
    def __init__(self, busNo, busDriver, driverPhone):
         self.__busNo = busNo
         self.__busDriver = busDriver
         self.__driverPhone = driverPhone
    def set_busNo(self, busNo):
       self.__busNo = busNo
    def set_busDriver(self, busDriver):
       self.__busDriver = busDriver
    def set_driverPhone(self, driverPhone):
        self.__driverPhone = driverPhone
        #the set method sets the atteibutes of class vehicle.
        #the get method returns the attributes of class vehicle.
    def get_busNo(self):
        return self.__busNo
    def get_busDriver(self):
        return self.__busDriver
    def get_driverPhone(self):
        return self.__driverPhone
    # The _ _str_ _ method returns the object's state
    # as a string.
    def __str__(self):
        return "Bus number:" + self.__busNo +  \
            "\n Bus driver:" + self.__busDriver + \
            "\n Driver number:" + self.__driverPhone
class seats:
    def __init__(self, noSeats, seatsNumbers):
        self.__noSeats = noSeats
        self.__seatsNumbers =seatsNumbers

    def set_noSeats(self, noSeats):
        self.__noSeats = noSeats
    def set_seatNumbers(self, seatNumbers):
        self.__seatsNumbers = seatNumbers
class date:
    def __init__(self, bookDate, travelDate):
        self.__bookDate = bookDate
        self.__travelDate = travelDate
    def set_bookDate(self, bookDate):
        self.__bookDate = bookDate
    def set_travelDate(self, travelDate):
        self.__travelDate = travelDate'''

# define global constants for main menu choices
create_ticket = 1
search_ticket = 2
edit_ticket = 3
delete_ticket = 4
exit_system = 5

FILENAME = 'tickets.dat'

import sys
def main():
    choice = 0
    while choice != exit_system:
        choice = menu_board()
        if choice == create_ticket:
            add()
        elif choice == search_ticket:
            search()
        elif choice == edit_ticket:
            edit()
        elif choice == delete_ticket:
            delete()
        elif choice == exit_system:
            sys.exit()
        else:
            print("invalid choice:")

def menu_board():
    print()
    print('Menu')
    print('---------------------------')
    print('1: add ticket')
    print('2: search ticket')
    print('3: edit ticket')
    print('4: Delete  ticket')
    print('5: Quit the program')
    print()
    choice = int(input('Enter your choice: '))
    while choice < create_ticket or choice > exit_system:
        choice = int(input('Enter a valid choice: '))
    return choice

def load_tickets(entry):
    try:
        # Open the tickets.dat file. as the files are passed as filename
        input_file = open(FILENAME, 'rb')
        tickets_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        tickets_dct = {}
        # Return the dictionary.
    return tickets_dct


def add():
    # Get the ticket info and passenger info.
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    # Create a passenger object named entry.
    entry = passenger(name, phone, email)
    # If the phone or email does not exist in the dictionary,
    # add it as a key reference of name with the entry object as the
    # associated value.

    if phone or email not in passenger:
        #  passenger[name] = entry
        save_tickets(entry)  # save ticket
        print('The ticket has been added.')
    else:
        print('That name already exists.')


def search():
    # Get a name to look up.
    name = input('Enter a name: ')
    # Look it up in the dictionary.
    try:
        pickle_in = open(name + ".txt", "rb")
        search_value = pickle.load(pickle_in)
       # flag = search_value.get_name()  # searching name in dictionary
        print(":passenger detais:")
        print(".............................")
        print("Name:"+ search_value.get_name())
        print("email:" + search_value.get_email())
        print("phone:" + search_value.get_phone())
        print("DONE!...........................")
    except:
        print('Name Not found')


def edit(passenger):
    name = input('Enter the name: ')

    if name in passenger:
        load_tickets(entry)
        #how to pass the taken name as input_file to load_tickets function.
 #how to load all the details here by using the above created load_tickets function by taking name as key value reference.
        print("enter the new details of ", name)
 #how to fetch just the name from that loaded informations of load_tickets functions.
        #now, delete the whole data from that loaded key name
        #after deleting that details now wecan add the new data as like same of add(passenger) function.

 #when this is done, it will be like almost same for the delete function.
        name = input('name:')
        phone = input('number: ')
        email = input('email address: ')
        entry = passenger(name, phone, email)
        #passenger[name] = entry
        if phone or email not in passenger:
            #  passenger[name] = entry
            save_tickets(entry)  # save ticket
            print('The ticket has been modified.')
        else:
            print('Sorry, error occoured.')

        print('ticket has been updated.')
    else:
        print('That name is not found.')

def delete(passenger):
    name = input('name: ')
    if name in passenger:
        del passenger[name]
        print('ticket deleted.')
    else:
        print('That name is not found.')

def save_tickets(entry):
    # Open the file for writing the object contents.
    file_name = entry.get_name()
    output_file = open(file_name + ".txt", 'wb')
    # Pickle the dictionary and save it
    pickle.dump(entry, output_file)
    output_file.close()

main()