HOw TO GET STARTED

step 1 -> Download the folder.
step 2 -> open todo.py file and in the imp_path variable place, put your path where you want to open/operate/create a text file.
          example1 -> 'D:/file_name1/file_name2/'
          example2 -> 'D:/new_folder/'

          remark* please use forward slash at the last of your path.

step 3(optional) -> put your email id, password and sender email id  at personal detailes (commented the section over there )

step 4 -> open command prompt or Windows terminal or windows terminal(admin)

step 5 -> write and press enter 

          .\todo.bat

step 4 -> now you are in the program.
          '$' dollar sing must be showing to you. now write and execute 
          
          ./todo

          it is a password . you can also change it.
step 5 -> whole menu will be infornt of you , now you can proceed.


(1)
HOW TO ADD TASK
for adding task command is ' ./todo add '  and  within under quotes write your task.
syntax ->   ./todo add "Your task here"    press enter.
example ->  ./todo add "watering plants"   press enter.
like this your task will be added in the queue.

(2)
HOW TO MARK DONE YOUR TASK
for marking done to your task, command is ' ./todo done ' and within under quotes write your task id.
syntax -> ./todo done task_id    press enter
example -> ./todo done 1     press enter
it will mark done to your task and will remove it from the to do queue and put it into done section.

(3)
HOW TO VIEW ALL THE TASKS
for seeing all the task, command is './todo ls'
example -> ./todo ls
and you will be able to see all your tasks.

(4)
HOW TO SEE REPORTS OF YOUR TASKS
for visulizing the tasks command is './todo report'
example -> ./todo report

(5)
HOW TO DELETE TASK
for deleting task command is ' ./todo del' and id of the task(which is wriiten before the task).
systax -> ./todo del task_id   press enter
example -> ./todo del 1        press enter

(6)
HOW TO SHARE THE TASKS
to share the tasks you need to enter sender and reciver address and sender's password to login to your account
. put your sender mail id on from_address named variable and reciver mail in to_address named variable. enter your password in password_of_from_id named variable.
I have commented you can take refrence.

for sharing command is './todo share' and the task id.
syntax -> ./todo share task_id
example -> ./todo share 1 

now press 'y' or 'n' according to your suitablity and hit enter.

(7)
HOW TO GET HELP OR ASSISTANT
for getting help, command is  './todo help'
example -> ./todo help 



remarks*
1. remark* please use forward slash at the last of your path.
2. there will some garbage value readed by the programm so delete those tasks and move on.