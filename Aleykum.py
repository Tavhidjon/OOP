from datetime import datetime

users = []
database = []

class User:
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.loggin = False

    def register(self):
        users.append(self)

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.loggin = True
            return True
        return False

    def logout(self):
        self.loggin = False

    def __str__(self):
        return f'User: {self.username}, Email: {self.email}'

class Task:
    id= 1
    def __init__(self, user, task_name, due_date, description, is_done=False):
        self.id = Task.id
        self.user = user
        self.task_name = task_name
        self.due_date = due_date
        self.description = description
        self.is_done = is_done
        self.created_at = datetime.now()
        Task.id+= 1

    def __str__(self):
        return f'User: {self.user.username}, Task: {self.task_name}, Due_date: {self.due_date}, Done: {self.is_done}'

class TaskManager:
    def __init__(self, istifodabaranda):
        self.istifodabaranda = istifodabaranda

    def add_task(self):
        if self.istifodabaranda.loggin:
            new_task = Task(
                self.istifodabaranda,
                input('Task name: '),
                input('Due date: '),
                input('Description: ')
            )
            database.append(new_task)
        else:
            print('Please login to add tasks.')

    def get_task_by_id(self, id):
        for task in database:
            if task.id == id and task.user == self.istifodabaranda:
                return task
        return None

    def get_all_tasks(self):
        for task in database:
            if task.user == self.istifodabaranda:
                print(task)

    def edit_task(self, id):
        task = self.get_task_by_id(id)
        if task:
            task.task_name = input('Task name: ')
            task.is_done = True
        else:
            print('Task not found or you do not have permission to edit this task.')

    def delete_task(self, id):
        task = self.get_task_by_id(id)
        if task:
            database.remove(task)
        else:
            print('Task yofta nashud ! .')


user1 = User('Tavhid', 'Vohidzoda', 'vohidzoda@gmail.com', 'tavhidjon', 'password1234')
user1.register()

if user1.login('tavhidjon', 'password1234'):
    print('Login successful!')
    manager = TaskManager(user1)

    while True:
        user_input = int(input('--> '))
        if user_input == 1:
            manager.add_task()
        elif user_input == 2:
            task = manager.get_task_by_id(int(input('Please enter task id: ')))
            if task:
                print(task)
            else:
                print('Task not found.')
        elif user_input == 3:
            manager.get_all_tasks()
        elif user_input == 4:
            manager.edit_task(int(input('Please enter task id to edit: ')))
        elif user_input == 5:
            manager.delete_task(int(input('Please enter task id to delete: ')))
        elif user_input == 6:
            user1.logout()
            print('Logged out.')
            break
        else:
            print('Please enter a number in range  1 to  6.')
