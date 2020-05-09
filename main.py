
staff_file = open("staff.txt", "a")
staff_file.write("\n")

staff_file.close()

login = True
login = input("Press '1' to login and '2' to close app: ")
if login == 1:
    print("Enter your username:\n ")
    login = False
else:
    print("Error! Invalid username. ")
if login == 2:
    print("Program ended! ")
    login = False

customer_acc_number = input('Enter Account Number: ')
staff_file = open('customer.txt', 'r').read()
if customer_acc_number in staff_file:
    first_line = staff_file.find('Account Number: '+customer_acc_number)
    customer_line = staff_file[first_line:]
    last_line = customer_line.find('---')
    customer_line = customer_line[:last_line]
    print(customer_line)
else:
    print('Customer not found!')
