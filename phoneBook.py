import datetime
import os


# call to exist contacts and calculate conversation time duration

def call_contact_func(contact_name, f):
    temp = 0
    for i in f:
        col = i.find(':')
        if i[:col] == contact_name:
            number = i[col + 1:-2]
            time1 = datetime.datetime.now()
            print('Calling ... ', number)
            print('If you want to end call, press Enter')
            input()
            time2 = datetime.datetime.now()
            delta_time = 'Call Duration = ' + str(time2 - time1)[:7]
            time1 = 'Call Time = ' + str(time1)[:19]
            f1 = open("log.txt", "a")
            f1.write(contact_name), f1.write(', '), f1.write(number), f1.write('\n')
            f1.write(time1), f1.write('\n')
            f1.write(delta_time), f1.write('\n\n')
            f1.close()
            print(time1)
            print(delta_time)
            temp = 1
    f.close
    if temp == 0:
        print('This name is not exist in number book')
        y = input('Do you want to add this contact Y/N : ')
        if y == 'y':
            get_contact_data()


# get new contact name and find iterative name

def get_contact_data():
    contact_name = input("Enter contact name:\n")
    if os.path.exists("contact_list.txt") is False:
        f = open("contact_list.txt", "w")
        f.close

    f = open("contact_list.txt", "r")
    temp = 0
    for x in f:
        col = x.find(':')
        if x[:col] == contact_name:
            temp = 1
    f.close

    if temp == 1:
        print('This name is already exist!, please enter again')
        y = input('Do want enter new name Y/N : ')
        if y == 'y':
            get_contact_data()

    if temp == 0:
        number = input('Enter contact Number: ')
        f2 = open("contact_list.txt", "a")
        f2.write(contact_name), f2.write(':'), f2.write(number)
        f2.write('\n')
        f2.close()


# display menu for you to add contact , call contact and etc.
def display_menu():
    get_input = input("Hi!\n1-If you want to call your contacts enter:" + "  call" + "\n" +
                      "2-If you want to display log of your calls enter:" + "  log" + "\n" +
                      "3-If you want to add contact to your contact list enter:" + "  add" + "\n"
                                                                                             "4-If you want to display all contact in your number enter:" + "  display" + "\n")
    return get_input


if __name__ == '__main__':

    if display_menu() == "call":
        name = input("Enter contact name:\n")
        f = open("contact_list.txt", "r")
        call_contact_func(name, f)

    if display_menu() == "log":
        log = input("Here is your recent calls:\n")
        if os.path.exists("log.txt") is False:
            f = open("log.txt", "w")
            f.close

        f = open("log.txt", "r")
        for i in f:
            print(i)
        f.close()

    if display_menu() == "add":
        get_contact_data()

    if display_menu() == "display":
        if os.path.exists("contact_list.txt") is False:
            f3 = open("contact_list.txt", "w")
            f3.close

        f3 = open("contact_list.txt", "r")
        for element in f3:
            print(element)
        f3.close()
