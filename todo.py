from datetime import date
import pyfiglet
import smtplib
my_file = open("todo.txt","w+")
imp_file = 'todo.txt'

#set your file path here.----------------------------------------------!
#or set your file path where you want a todo.txt file------------------!
imp_path = 'D:/app_final/'



cust_path = f'{imp_path}{imp_file}' #important


#function for providing time and date
def give_time():
    today = date.today()
    return today


#function for counting all your pending tasks.
def pending_completed_counter():
    count_1 = 0
    counter_2 = 0
    # opening todo_list.txt file
    pending = open(cust_path, 'r')
    for line in pending:
        count_1 = count_1 + 1
    pending.close()
    # opening done_list.txt file
    completed = open(cust_path, 'r')
    for lines in completed:
        counter_2 = counter_2 + 1
    completed.close()
    return count_1, counter_2  # returning the pending and completed numbers of each file


#function for printing the report
def print_report():
    date_1 = give_time()
    pending_completed = pending_completed_counter()
    print(f'{date_1} Pending : {pending_completed[0]}  completed : {pending_completed[1]}')

#function for provding the menu in every click
def print_menu():
    print('$ Usage :-')
    print('$ ./todo add "todo item"    #Add a new todo')
    print('$ ./todo ls                 #Show remaining todos')
    print('$ ./todo del NUMBER         #Delete a todo')
    print('$ ./todo done NUMBER        #Complete a todo')
    print('$ ./todo help               #Show usage')
    print('$ ./todo report             #Statistics')
    print('$ ./todo share              #Share to your friends')


def add_el(str_var):
    temp = str_var
    f = open(cust_path, 'a')
    f.write('\n' + temp)
    f.close()


def print_ls():  # prints all the valid lists present in the .txt file
    def rev():  # calculates the total number of lists
        f1 = open(cust_path, 'r')
        count2 = 0
        for m in f1:
            count2 = count2 + 1
        f1.close()
        return count2
    f = open(cust_path, 'r')
    gth = rev()
    count1 = gth  # iterating from reverse(reverse counting)
    for j in f:
        print(f"[{count1}] {j}", end="")
        count1 = count1 - 1  # iterating from reverse
    f.close()


#marks every task as done and remove from the queue and move to the done section.
def done_el(num):
    cd = []
    f1 = open(cust_path, 'r')
    for line in f1:
        cd.append(line)
    f1.close()
    num_var = len(cd) - num
    # var = num - 1  # index to be deleted
    var2 = cd[num_var]  # storing the value to shift into done list
    cd.pop(num_var)  # item is now deleted
    f2 = open(cust_path, 'w')  # writing operation is going to perform
    for ln in range(len(cd)):
        f2.write(cd[ln])
    f2.close()
    # storing the done list into the file
    f3 = open(cust_path, 'a')
    f3.write(var2)
    f3.close()


#remove the task from the queue 
def del_it(num):
    lg = []
    f12 = open(cust_path, 'r')
    for line in f12:
        lg.append(line)
    f12.close()
    num_var = len(lg) - num
    lg.pop(num_var)
    f13 = open(cust_path, 'w')
    for ln in range(len(lg)):
        f13.write(lg[ln])
    f13.close()

#function for establishing and secure connection and sending the files.
def share_task():
    lg = []
    # --------------Personal Detailes to be filled here---------------!
    to_address = "example@gmail.com"
    from_address = "example_two@gmail.com"
    password_of_from_id = "password"
    #--------------Caution here-----------------------------------!
    f12 = open(cust_path, 'r')
    for line in f12:
        lg.append(line)
    f12.close()
    var4 = int(input("Enter the id of task to be shared :")) # taking index in input
    var6 = lg[len(lg) - var4]; #passing this in the content of email
    print(f"Task will be send To :{to_address} From : {from_address}")
    var5 = str(input("Press y to continue and n to discard"))
    if var5 == "n" or var5 == "N":
        print("Process Discarded")
    else:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(from_address,password_of_from_id)
        server.sendmail(from_address,to_address,f"Hello ther, Todo here!\n{var6}\n\nIf you want to contribute"
        "or suggest some modification in this task then you can reply to this mail.\n Thank you. ")
        server.quit()



if __name__ == '__main__':
    while 1:
        start = str(input("$ "))
        if start == './todo':  # starter
            result = pyfiglet.figlet_format("Welcome")
            print(result)
            print_menu()
            while 1:
                command = ['./todo add', './todo ls', './todo del ', './todo done', './todo help', './todo report','./todo share']
                index = 0
                count = 0
                command_input = str(input("\n$ "))
                com1 = command_input[:11]
                c = len(command_input) - 1
                com2 = command_input[12:c]
                com3 = command_input[12:]
                com4 = command_input[10:]
                com5 = command_input[:13]


                # print(com1)
                # print(com2)
                for i in range(len(command)):  # confirming that command is valid
                    if command[i] == com1 or command[i] == com5:
                        index = i

                variable = index
                #print(variable)

                if variable == 0:
                    count = count + 1
                    add_el(str(com2))
                    print(f'Added todo: "{com2}"')
                if variable == 1:
                    print_ls()
                if variable == 2:
                    del_it(int(com4))
                    print(f"Deleted todo #{com4}")
                if variable == 3:
                    var1 = int(com3)
                    done_el(var1)
                    print(f"Marked todo #{var1} as done.")
                if variable == 4:
                    print_menu()
                if variable == 5:
                    print_report()
                if variable == 6:
                    share_task()




