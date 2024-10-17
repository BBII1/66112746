task = ["clean the house", "shopping"]
def add_task(task,new_tasks):
    task.append(new_tasks)
    return task

print("เพิ่ม 'math homework' ในลิสต์ task :",add_task(task,"math homework"))

