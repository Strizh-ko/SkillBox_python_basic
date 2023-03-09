class Stack:

    def __init__(self, real_lst=None):
        if not real_lst:
            self.real_lst = list()
        else:
            self.real_lst = real_lst
        self.str_lst = self.str_copy(self.real_lst)

    def __str__(self):
        return ' > '.join(self.str_lst)

    def add(self, elem):
        self.real_lst.insert(0, elem)
        self.str_lst = self.str_copy(self.real_lst)

    def delete(self, elem):
        i = self.real_lst.index(elem)
        self.real_lst = self.real_lst[i:]
        self.real_lst.remove(elem)
        self.str_lst = self.str_copy(self.real_lst)

    def str_copy(self, real_lst):
        return [str(e) for e in real_lst]


class TaskManager:
    tasks = dict()

    def __str__(self):
        stack = Stack(self.task_lst)
        out = '\n'.join(stack.str_lst)
        return str(out)

    def new_task(self, task, n):
        if self.tasks.get(n):
            self.tasks[n] += f', {task}'
        else:
            self.tasks[n] = task
        self.task_lst = [str(i) + ' ' + str(e) for i, e in self.tasks.items()]
        self.task_lst = sorted(self.task_lst)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
