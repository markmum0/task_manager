# first to create a class for the tasks
class Task:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def __str__(self):
        return '{} : {}'.format(self.title, self.date)


class Taskmanager:
    def __init__(self):
        self.tasks = []

    # adding a task and date
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def __str__(self):
        tasks_left = [str(task) for task in self.tasks]
        return '\n'.join(tasks_left)


duty_1 = Task('Do the laundry', '22-01-2024')
duty_2 = Task('Do the dishes', '22-01-2024')

task_manager = Taskmanager()
task_manager.add_task(duty_1)
task_manager.add_task(duty_2)

task_manager.remove_task(duty_2)
print(task_manager)
