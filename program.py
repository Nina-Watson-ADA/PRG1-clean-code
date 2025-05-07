def create_task(task_list, task_name, task_due):
    t = {'name': task_name, 'date': task_due, 'completed': False}
    task_list.append(t)

def filter_tasks(task_list, task_name):
    return [t for t in task_list if t['name'] != task_name]

def print_tasks(task_list):
    print("All Tasks:")
    for t in task_list:
        print(f"Task: {t['name']}, Due: {t['date']}, Completed: {t['completed']}")

def complete_tasks(task_list, task_name):
    try:
        task_index = next(i for i, t in enumerate(task_list) if t['name'] == task_name)
        task_list[task_index]['completed'] = True
    except StopIteration:
        print("Task not found.")

task_list = []

create_task(task_list, "Fix bug in code", "2024-02-21")
create_task(task_list, "Update documentation", "2024-02-22")
print_tasks(task_list)
complete_tasks(task_list, "Fix bug in code")
task_list = filter_tasks(task_list, "Update documentation")  
print_tasks(task_list)
