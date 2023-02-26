import datetime
import os.path

GREEN = "\033[92m"
LIGHTRED = "\033[91m"
WHITE = "\033[0m"
CYAN = "\033[96m"

password_file = open("user.txt", "r")
task_file = open("tasks.txt", "r")

# ===Functions====
# Registering a new user:


def reg_user():
    with open("user.txt", "r+") as file:
        data = file.readlines()
        user_names = [line.split(", ")[0] for line in data]
        while True:
            print("To register a new user we will require the following information:\n")
            new_username = input("What is the username? ")
            if new_username not in user_names:
                new_password = input("What is the password? ")
                new_password_confirm = input("Please confirm the password: ")
                if new_password == new_password_confirm:
                    print(f"{GREEN}Success: User now registered!{WHITE}\n")
                    file.write(f"{new_username}, {new_password}\n")
                    break
                else:
                    print(
                        f"{LIGHTRED}Your passwords do not match. Please try again.{WHITE}\n")
            elif new_username in user_names:
                print(
                    f"{LIGHTRED}This user name already exists, please add a user with a different username{WHITE}\n")

# Adding a task:


def add_task():
    with open("tasks.txt", "a") as file:
        now = datetime.datetime.now()
        current_time = now.strftime("%d %b %Y")
        print(
            "To add a new task we will require the following information:\n")
        user_name = input(
            "What is the username of the person to whom the task is assigned? ")
        title = input("What is the title of the task? ")
        description = input("What is the task description? ")
        due_date = input("What is the task due date? ")
        file.write(
            f"\n{user_name}, {title}, {description}, {current_time}, {due_date}, No")
        print(f"{GREEN}Success: New task added! {WHITE}\n")

# View all tasks:


def view_all():
    with open("tasks.txt", "r") as file:
        data = file.readlines()
        for count, line in enumerate(data, start=1):
            split_data = line.split(", ")
            print(
                f"╔═══════════════════════════════════════════════ Task {count} ══════════════════════════════════════════════════════════╗")
            print(f"    Task:\t\t{split_data[1]}")
            print(f"    Assigned to:\t{split_data[0]}")
            print(f"    Date Assigned:\t{split_data[3]}")
            print(f"    Due Date:\t\t{split_data[4]}")
            print(f"    Task Complete?\t{split_data[5]}")
            print(f"    Task Description:\n    {split_data[2]}")
            print(
                "╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\n\n")

# View assigned tasks:


def view_mine():
    with open("tasks.txt", "r") as file:
        data = file.readlines()
        user_names = [line.split(", ")[0] for line in data]
        if entered_username in user_names:
            counter = [12]
            count = 0
            user_tasks = []
            task_indexes = []
            for index, line in enumerate(data):
                split_data = line.split(", ")
                if entered_username == split_data[0]:
                    count += 1
                    user_tasks.append(split_data)
                    task_indexes.append(index)
                    counter.append(count)
                    print(
                        f"╔═══════════════════════════════════════════════ Task {count}:{entered_username} ═══════════════════════════════════════════════════╗")
                    print(f"    Task:\t\t{split_data[1]}")
                    print(f"    Assigned to:\t{split_data[0]}")
                    print(f"    Date Assigned:\t{split_data[3]}")
                    print(f"    Due Date:\t\t{split_data[4]}")
                    print(f"    Task Complete?\t{split_data[5]}")
                    print(
                        f"    Task Description:\n    {split_data[2]}")
                    print(
                        "╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\n\n")
            while True:
                task_number = int(
                    input("If you would like to edit a task, please type the task number or type -1 to exit: "))
                if task_number in counter:
                    if user_tasks[task_number-1][-1] == "No\n":
                        to_complete = input(
                            ("This task is not complete. Would you like to mark as complete? y/n: "))
                        if to_complete.lower() == "y":
                            user_tasks[task_number-1][-1] = "Yes\n"
                            data[task_indexes[task_number-1]
                                 ] = ", ".join(user_tasks[task_number-1])
                            with open("tasks.txt", "w") as fileout:
                                fileout.writelines(data)
                            print(
                                f"{GREEN}This task has now been marked as complete{WHITE}")
                            break
                        elif to_complete.lower() == "n":
                            to_edit = input('''What would you like to edit:
                            u - change username
                            dd - change due date: ''')
                            if to_edit.lower() == "u":
                                new_username = input(
                                    "What is the new username for this task? ")
                                user_tasks[task_number-1][0] = new_username
                                data[task_indexes[task_number-1]
                                     ] = ", ".join(user_tasks[task_number-1])
                                with open("tasks.txt", "w") as fileout:
                                    fileout.writelines(data)
                            elif to_edit.lower() == "dd":
                                new_deadline = input(
                                    "What is the new deadline for this task? ")
                                user_tasks[task_number-1][4] = new_deadline
                                data[task_indexes[task_number-1]
                                     ] = ", ".join(user_tasks[task_number-1])
                                with open("tasks.txt", "w") as fileout:
                                    fileout.writelines(data)
                    else:
                        print(
                            f"{LIGHTRED}You cannot edit a completed task{WHITE}")
                        break
                elif task_number == -1:
                    break
                elif task_number != count:
                    print(
                        f"{LIGHTRED}This is not a valid task number. Try again.{WHITE}")
        elif entered_username not in user_names:
            print(
                f"{LIGHTRED}The logged in user doesn't have tasks to display{WHITE}")

# View Statistics


def run_reports():
    if os.path.isfile("task_overview.txt") and os.path.isfile("user_overview.txt"):
        with open("task_overview.txt", "r") as task_file, open("user_overview.txt", "r") as user_file:
            task_data = task_file.readlines()
            user_data = user_file.readlines()
            print(
                f"╔════════════════════════════════════ Task Statistics ═══════════════════════════════════════════╗")
            for line in task_data:
                print("".join(line).strip("\n"))
            print(
                "╚════════════════════════════════════════════════════════════════════════════════════════════════╝\n\n")
            print(
                f"╔════════════════════════════════════ User Statistics ═══════════════════════════════════════════╗")
            for line in user_data:
                print("".join(line).strip("\n"))
            print(
                "╚════════════════════════════════════════════════════════════════════════════════════════════════╝\n\n")

    else:
        generate_reports()
        run_reports()

# Generating Reports


def generate_reports():
    task_file = open("tasks.txt", "r")
    user_file = open("user.txt", "r")
    with open("task_overview.txt", "w") as task_overview_file, open("user_overview.txt", "w") as user_overview_file:
        task_data = task_file.readlines()
        user_data = user_file.readlines()
        total_tasks = len(task_data)
        task_list = [line.split(", ") for line in task_data]
        completion_list = [line.split(", ")[5].strip("\n")
                           for line in task_data]
        deadline_list = [line.split(", ")[4].strip("\n")
                         for line in task_data]
        now = datetime.datetime.now()
        incomplete_count = 0
        complete_count = 0
        overdue_count = 0
        overdue_incomplete_count = 0
        for entry in completion_list:
            if entry.lower() == "no":
                incomplete_count += 1
            elif entry.lower() == "yes":
                complete_count += 1
        for entry in deadline_list:
            entry = datetime.datetime.strptime(entry, "%d %b %Y")
            if now > entry:
                overdue_count += 1
        for entry in task_list:
            deadline = datetime.datetime.strptime(entry[4], "%d %b %Y")
            if now > deadline and entry[5].lower().strip("\n") == "no":
                overdue_incomplete_count += 1

        task_overview_file.write(
            f"Total number of tasks generated and tracked: {total_tasks}\n")
        task_overview_file.write(
            f"Total number of completed tasks: {complete_count}\n")
        task_overview_file.write(
            f"Total number of uncompleted tasks: {incomplete_count}\n")
        task_overview_file.write(
            f"Total number of overdue tasks that are incomplete: {overdue_incomplete_count}\n")
        task_overview_file.write(
            f"Percentage of tasks incomplete: {round((incomplete_count/total_tasks)*100 ,2)}%\n")
        task_overview_file.write(
            f"Percentage of tasks overdue: {round((overdue_count/total_tasks)*100 ,2)}%\n")
        user_overview_file.write(
            f"Total number of users registered: {len(user_data)}\n")
        user_overview_file.write(
            f"Total number of tasks generated and tracked: {total_tasks}\n")

        user_names = [line.split(", ")[0] for line in user_data]
        for user in user_names:
            final_user_count = 0
            user_count = 0
            user_complete = 0
            user_incomplete = 0
            user_overdue_incomplete_count = 0
            for line in task_data:
                task_info = line.split(", ")
                if user in task_info:
                    user_count += 1
                    final_user_count += 1
                    if "Yes" in task_info[5]:
                        user_complete += 1
                    if "No" in task_info[5]:
                        deadline = datetime.datetime.strptime(
                            task_info[4], "%d %b %Y")
                        user_incomplete += 1
                        if now > deadline:
                            user_overdue_incomplete_count += 1

            user_overview_file.write(f"\n{user.upper()}")
            user_overview_file.write(
                f"\n Total number of tasks assigned to user: {user_count}")
            user_overview_file.write(
                f"\n Percentage of tasks assigned to user: {round((user_count/total_tasks)*100,2)}%")
            user_overview_file.write(
                f"\n Completed tasks: {round((user_complete/final_user_count)*100,2)}%")
            user_overview_file.write(
                f"\n Incomplete tasks: {round((user_incomplete/final_user_count)*100,2)}%")
            user_overview_file.write(
                f"\n Overdue and Incomplete: {round((user_overdue_incomplete_count/final_user_count)*100,2)}%")

        print(f"{GREEN}Success: New reports generated! {WHITE}\n")


# Login Section
# The program reads usernames and passwords from the user.txt file
# If both the inputted username and password match the data in the user.txt file, the menu of options is displayed.
# If the user logs in as 'admin' a specific menu is displayed.
# A while loop is used to repeatedly ask the user for their username and password until there is a match.
print("═════════════ Task Management System ══════════════")
print("                 PLEASE LOG IN                     ")
print("═══════════════════════════════════════════════════")

user_data = password_file.readlines()

while True:
    entered_username = input("\nWhat is your username? ")
    entered_password = input("What is your password? ")
    admin = False
    for line in user_data:
        login_pair = line.split(", ")
        username = login_pair[0]
        password = login_pair[1].strip("\n")
        if entered_password == password and entered_username == username and entered_username == "admin":
            print(f"{GREEN}Login Successful!")
            admin = True
        elif entered_password == password and entered_username == username and entered_username != "admin":
            print(f"{GREEN}Login Successful!")
            admin = False
        else:
            continue

        # Menu Option (admin)
        while True:
            if admin == True:
                print(
                    f"\n{CYAN}═════════════════════MENU═════════════════════════{WHITE}")
                menu = input('''Select one of the following options below:
💠 r  - Register a user
💠 a  - Add a task
💠 va - View all tasks
💠 vm - View my tasks
💠 gr - Generate reports
💠 ds - Display statistics
💠 e  - Exit
══════════════════════════════════════════════════
: ''').lower()
            # Menu Option (all other users)
            elif admin == False:
                print(
                    f"\n{CYAN}═════════════════════MENU═════════════════════════{WHITE}")
                menu = input('''Select one of the following options below:
💠 r  - Register a user
💠 a  - Add a task
💠 va - View all tasks
💠 vm - View my tasks
💠 e  - Exit
══════════════════════════════════════════════════
: ''').lower()

            # Function calling for all the different menu options
            if menu == "r" and entered_username == "admin":
                reg_user()

            elif menu == "a":
                add_task()

            elif menu == "va":
                view_all()

            elif menu == "vm":
                view_mine()

            elif menu == "ds" and entered_username == "admin":
                run_reports()

            elif menu == "gr" and entered_username == "admin":
                generate_reports()

            elif menu == "e":
                print("Goodbye!!!")
                password_file.close()
                task_file.close()
                exit()

            # Error statements
            else:
                if menu == "r" and entered_username != "admin":
                    print(
                        f"{LIGHTRED}Only the admin is allowed to register users. Please choose another option or exit and alog in as admin.{WHITE}")
                else:
                    print(
                        f"{LIGHTRED}You have made a wrong choice! Please try again!{WHITE}")
    else:
        print(f"{LIGHTRED}Login Unsuccessful! Please try again!{WHITE}")
        continue
