# Cоздай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self,name_task,task_description,due_date,):
        self.name_task = name_task
        self.task_description = task_description
        self.due_date = due_date
        self.status = "не выполнено"

    list_current_unfulfilled_task = []

    def adding_tasks(self):
       # Добавляем текущую задачу в список задач
        Task.list_current_unfulfilled_task.append(self)
        print(f"Задача ‘{self.name_task}‘ добавлена.")

    def marking_completed_tasks(self):
        self.status = "выполнено"
        print(f"Задача‘{self.name_task}‘ выполнена")

    def display_task_info(self):
        print(f"Название: {self.name_task}")
        print(f"Описание: {self.task_description}")
        print(f"Дата выполнения: {self.due_date}")
        print(f"Статус: {self.status}")


task1 = Task("Покупка продуктов", "Купить хлеб и молоко", "2025-01-09")
task2 = Task("Вып-е домашки", "Отправить домашку на проверку", "2025-01-09")

task1.adding_tasks()
task2.adding_tasks()

# Отображаем информацию о задачах
task1.display_task_info()
task2.display_task_info()

# Отмечаем задачу как выполненную
task1.marking_completed_tasks()

# Проверяем статус задачи после выполнения
task1.display_task_info()

task3 = Task("Проверка рабоы class Task","Убеждение работы","2025-01-10")
task3.adding_tasks()
task3.marking_completed_tasks()
task3.display_task_info()








