class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."

  def get_net_salary(self):
    self.net_salary = self.salary - (self.salary * 0.15 + self.children * 1500)
    return f"Čistý plat má {self.net_salary} Kč, protože má počet dětí: {self.children}."

  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = salary
    self.children = children

frantisek = Employee("František Novák", "Konstruktér", 55000, 2)
klara = Employee("Klára Nová", "recepční", 30000, 1)

print(frantisek.get_info())
print(frantisek.get_net_salary())
print(klara.get_info())
print(klara.get_net_salary())