from datetime import datetime
database = []
class Task:
    id=0
    def __init__(self,user,task_name,due_date,description,is_done=False):
        self.id+=1
        self.user = user
        self.task_name=task_name
        self.due_date=due_date
        self.description=description
        self.is_done=is_done
        self.created_at = datetime.now
        Task.id+=1
    def __str__(self):
        return f'{self.user}{self.task_name}{self.due_date}{self.is_done}'

class TaskManager:
    def add_task(self):
        new_task = Task (
                         
            input('username: '),
            input('Task name: '),
            input('Due_datetime'),
            input('Description')      
        )
        database.append(new_task)
    
    def get_task_by_id(self,id):
        for task in database:
            if task.id == id:
                return task
    
    def get_all_tasks(self):
        for task in database:
            print(task)

    def edit_task(self,id):
        task=self.get_task_by_id(id)
        task.task_name=input('Task_name ')
        task.is_done=True

    def delete_task(self,id):
        task=self.get_task_by_id(id)
        database.remove(task)

manager =TaskManager()
while True:
    user_input =int(input('-->'))
    if user_input==1:
        manager.add_task()
    elif user_input ==2:
        task =manager.get_task_by_id(
            int(input('Please enter task id:'))
        )
        print(task)
    elif user_input == 3:
        manager.get_all_tasks()
    elif user_input == 4:
        manager.edit_task(
            int(input('Please enter task id to edit: '))
        )
    elif user_input == 5:
        manager.delete_task(
            int(input('Please enter task id to delete: '))
        )
    elif user_input == 6:
        break
    else:
        print('please enter task in range 1 to 6 :')






