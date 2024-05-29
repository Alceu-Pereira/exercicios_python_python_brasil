class Employee:
    def __init__(self, name, salary):
        self.name = str(name)
        self.salary = float(salary)

    def show_name(self):
        print(f'O nome do funcionário é {self.name}')

    def show_salary(self):
        print(f'O funcionário recebe um salário de R$ {self.salary:.2f}')


funcionario = Employee('Alceu', 2100)
funcionario.show_name()
funcionario.show_salary()