class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)  



    @classmethod  
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    @classmethod 
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #line that creates a new employee

class Developer(Employee):
      raise_amt =1.10
      def __init__(self,first,last,pay,prog_lang):
          super().__init__(first,last,pay)
          self.prog_lang = prog_lang
class Manager(Employee):
    def __init__(self,first,last,pay,employees= None):
        super().__init__(first,last,pay) 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

isinstance() # is name an instance of the class

          

dev_1 = Developer('corey','shafur',5000000, "Py")
dev_2 = Developer('carry','noname',700000, "Java")

# print(help(Developer)) func to use for info abt inherrited class
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
print(dev_1.prog_lang) 

