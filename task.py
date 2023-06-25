class Task:
    """Represents a project task"""
    def __init__(self):
        self.task_description = ''
        self.task_estimations = []
        self.chosen_estimation = 0
        self.add_description()
        self.add_estimations()

    def add_description(self):
        print('Please enter a task description:\n')
        self.task_description = input()

    def add_estimations(self):
        for i in range(3):
            estimate = input(f"Please enter the {i + 1} effort estimation for task in man.hours:\n")
            self.task_estimations.append(int(estimate))

    def add_chosen_estimation(self):
        self.chosen_estimation = int(input("\nPlease enter your chosen estimate:\n"))