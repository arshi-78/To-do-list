import shutil # import shutil for terminal width

# this function will print the text stored in text variable in center
def centerd(text):
    terminal_width = shutil.get_terminal_size().columns #get a terminal width
    return f"{text.center(terminal_width)}"

# this function will provide validitation check for users input

def user_choice():
    choice = input("Kindly enter the number Of tasks you want to add = ")
    while True:
        # number_of = input("Kindly Enter The Number Of Task You Want To Add = ")
        if choice.isdigit():
            choice=int(choice)
            break
            #pass # Exit the loop if input is valid
        else:
            print("Invalid input. Kindly enter a valid integer.")
            choice = input("Kindly enter the number of tasks you want to add = ")
    return choice


 # CODE TO ADD THE TASKS USER WANTS TO ENTER


# Text to be printed in center of the terminal
text = "\033[1m-: WELCOME TO 'TO DO LIST' APPLICATION :-\033[0m"
print(centerd(text))
print()

number_of_tasks=user_choice()  # here the function is called
        
# Gives a blank line
print()

initial_tasks_list = []

# take the tasks input that user wanted to add to the list

for i in range(number_of_tasks):
    element = input(f"Enter task no {i + 1}: ")  
    initial_tasks_list.append(element)

# Gives a blank line
print()

print("Forgot to add a task? :( .Don't worry I got you ! :) ")
print()

# print(" forget to add a task :( .Don't worry I got you ! ")

n = input("Enter \033[1m'Y'\033[0m if you want to add more tasks or enter \033[1m'N'\033[0m to finish: ").upper()

# Gives a blank line
print()
while n!="Y" and n!="N":  # VALIDITATION CHECK
    print("invalid input")
    n = input("Enter \033[1m'Y'\033[0m if you want to add more tasks or enter \033[1m'N'\033[0m to finish: ").upper()

# this code will add more tasks to the list if user wants

if n=='Y':

    s = user_choice() # function is called

    # Gives a blank line
    print()

    # prints the final tasks that user wants
    for j in range(s):
        element1 = input(f"Enter task no {number_of_tasks + j + 1}: ")  
        initial_tasks_list.append(element1)

 # if the user does not want to add his list the program will run as usual
elif n=='N':
    pass
 
# Gives a blank line
print()


  # PRINT THE TASK LIST


# Text to be printed in center
text="\033[1m-: YOUR TO DO LIST :-\033[0m"
print(centerd(text))

text=" NOTE : If a task is added multiple times it will be automatically removed from the list"
print(centerd(text))
print()

# here the function remove_duplicates will remove the duplicates from the existing list 

tasks_list=[]
def remove_duplicates(initial_tasks_list):
    for i in initial_tasks_list:
        if i not in tasks_list:
            tasks_list.append(i)
    return tasks_list

remove_duplicates(initial_tasks_list)  # here function is called
z=1
for task in tasks_list:  # loop to print the tasks that user enters
    print("Your task no:",z,f" is: {task}")
    z+=1

# Gives a blank line
print()

# CODE TO REMOVE A TASK FROM A LIST


text="\033[1m-: REMOVING A TASK FROM THE LIST :-\033[0m"
print(centerd(text))
print()


t = input("Enter \033[1m'Y'\033[0m if you want to remove a tasks from your list or enter \033[1m'N'\033[0m : ").upper()

# here t is choice of user if he wants to remove a task or not

print()
while t!="Y" and t!="N": # VALIDITATION CHECK
    print("invalid input")
    t = input("Enter \033[1m'Y'\033[0m if you want to remove a tasks from your list or enter \033[1m'N'\033[0m  : ").upper()

if t=="Y":
    print()
    task_to_remove=input("Enter the task you want to remove from the list if you wish to remove two or more task than seperate them by a comma ' , '  : ")

    task_to_remove = [task.strip() for task in task_to_remove.split(',')]  # this comand is taken from chatgpt 
    

    # task.strip() removes extra spaces from the start and end of a task name, ensuring consistency and preventing errors 
    # The split(',') method divides the string at each comma resulting in a list where each element is a task as entered by the user

    print()
    for i in task_to_remove:   # loop to remove a certain task from the list that user wants
        if i in tasks_list:

            tasks_list.remove(i)
            print(f" The task '{i}' has been removed from the list ! ")
            print()

        else:
            print(f"The given task '{i}' is not in the list ! ")
            print()
else:
    pass


# CODE TO CHECK THE STATUS OF YOUR TASKS


text="\033[1m-: CHECKING THE STATUS OF YOUR TASKS:-\033[0m"
print(centerd(text))
print()

tasks_response=[]  # list to store the users response

for task in tasks_list:
    response=input(f" Is the task \033[1m'{task}'\033[0m done? Kindly enter \033[1m'Y'\033[0m for yes or \033[1m'N'\033[0m for no to mark the status of your task: ").upper()
    
    while response!="Y" and response!="N":
        print(" invalid input")
        response=input(f" Is the task \033[1m{task}\033[0m done? Kindly enter \033[1m'Y'\033[0m for yes or \033[1m'N'\033[0m for no to mark the status of your task: ").upper()


    if response=='Y':
        tasks_response.append((task,"= This task is done :) "))
    elif response=='N':
        tasks_response.append((task,"= This task is not done :( "))
    

print()
# Print the tasks list


# TO PRINT THE LIST ALONG WITH THE STATUS OF THE TASK


text="\033[1m-: STATUS OF YOUR TO DO LIST :-\033[0m"
print(centerd(text))

u=1
for task, status in tasks_response:
    print(" Your task no",u,":",f" {task} {status}")
    u+=1
print() 

