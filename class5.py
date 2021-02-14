class Employee:
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay   = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp) 

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())
    
    def __repr__(self):
        return "{self.__class__.__name__}({self.first},{self.last},{self.pay})".format(self=self)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
       



dev_1 = Developer('Mustafa','Al_Ogaidi',50000,'Python')
dev_2 = Developer('Mena','Al_Ogaidi',60000,'Java')
dev_3 = Developer('Yousif','Al_Ogaidi',70000,'C++')

mgr_1 = Manager('Sue','Smith',90000,[dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(mgr_1)
print(mgr_1.__repr__())
print(mgr_1.__str__())
#print('---------------')
#
#print(isinstance(mgr_1,Manager))
#print(isinstance(mgr_1,Developer))
#print(isinstance(mgr_1,Employee))
#print(isinstance(Manager,Employee))
#print(mgr_1.__repr__())
#print(dev_1.email)
#print(dev_1.prog_lang)
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

#print(help(Developer))

#import datetime
#my_date = datetime.date(2016,7,11)

#emp_1 = Employee('Mustafa','Al Ogaidi',5000)
#emp_2 = Employee('Mena','Al Ogaidi',6000)

#print(Employee.is_workday(my_date))

#emp_str_1 = "Jhon-Doe-70000"
#emp_str_2 = "Jane-Doe-90000"
#emp_str_3 = "Steven-Smith-30000"
#emp_3 = Employee.from_string(emp_str_2)
#
#print(emp_3.pay,emp_3.email,emp_3.fullname())
#Employee.set_raise_amt(1.5)

#print(emp_1.pay)
#print(emp_1.fullname())
#print(emp_1.apply_raise())
#emp_1.raise_amount = 1.05
#print(Employee.__dict__)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)
#print(Employee.num_of_emp)

