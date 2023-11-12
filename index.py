#
class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

# Abaixo está uma Função para validar a prioridade
def validate_priority(priority):
    return 1 <= priority <= 5


# Abaixo está o controlador das tarefas
class TaskController:
    tasks = []

    @classmethod
    def add_task(cls, task):
        cls.tasks.append(task)

    @classmethod
     # Função para visualizar as tarefas
    def view_tasks(cls):
        for task in cls.tasks:
            print(f"Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")

   

# Abaixo é uma interface para criação das tarefas e prioridades
class ConsoleUI:
    @staticmethod
    def get_task_input():
        description = input("Digite a descrição da tareda: ")
        due_date = input("Digite a Data: ")
        priority = int(input("Digite a Prioridade (de 1 a 5): "))
        return Task(description, due_date, priority)


def main():
    while True:
        print("\n1. Adicionar tarefa\n2. Ver tarefas\n3. sair")
        choice = input("Digite sua Escolha: ")

        if choice == "1":
            task = ConsoleUI.get_task_input()
            if validate_priority(task.priority):
                TaskController.add_task(task)
            else:
                print("Priorização inválida, você deve escolher algo entre 1 e 5.")
        elif choice == "2":
            TaskController.view_tasks()
        elif choice == "3":
            break
        else:
            print("Escolha inválida. Tente Novamente")


if __name__ == "__main__":
    main()