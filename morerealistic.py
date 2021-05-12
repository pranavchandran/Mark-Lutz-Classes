# More Realistic 
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
        
# bob = Person('Bob Smith')
# sue = Person('Sue', job='dev', pay=100000)
# print(bob.name, bob.pay)
# print(sue.name, sue.pay)

# for test purpose
# if __name__ == '__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob.name, bob.pay)
#     print(sue.name, sue.pay)

# Adding behaviour methods
# ----
# Coding methods
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1+percent))
        
# if __name__ == '__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob.name, bob.pay)
#     print(sue.name, sue.pay)
#     print(bob.lastName(), sue.lastName())
#     # Use the new methods
#     sue.giveRaise(.10)
#     # instead of hardcoding
#     print(sue.pay)
#     print(sue)

# Add representation overloading method
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#     def __repr__(self):
#         return '[Person: %s %s]' %(self.name, self.pay)
        
# Add a manager class inherits Person
# ML telling its a bad way
# class Manager(Person):
#     def giveRaise(self, percent, bonus=.10):
#         self.pay = int(self.pay * (1+percent + bonus))

# ML telling its the best way
# class Manager(Person):
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise((self, percent + bonus))

# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#     def __repr__(self):
#         return '[Person: %s, %s]' % (self.name, self.pay)
# class Manager(Person):
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise(self, percent + bonus)
#     def somethingelse(self, leave=0):
#         if leave > 0:
#             l = leave * 1000
#             print(f'Leave will reduce the amount from salary of {l}')
#             self.pay -= l
        
# Polymorphism in Action
'''
# Customizing constructors too
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
        
# class Manager(Person):
#     def __init__(self, name, pay):
#         Person.__init__(self, name, 'mgr', pay)
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise(self, percent + bonus)

# other ways to combine classes
class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent+bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __repr__(self):
        return str(self.person)
        
class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
            
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)
    
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
    
# if __name__ == '__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
    # print(bob)
    # print(sue)
    # print(bob.lastName(), sue.lastName())
    # sue.giveRaise(.10)
    # print(sue, bob)
    # man1 = Manager('usef ali', pay=200000)
    # man1.giveRaise(.10)
    # print(man1.lastName())
    # print(man1.pay)
    # print(man1)
    # print('--All three--')
    # for obj in (bob, sue, man1):
    #     obj.giveRaise(.10)
    #     print(obj)
    # print(man1.somethingelse((80)))
    # print(man1)
    
    
# Using Introspection Tools
# Special Class Attributes

print(bob.__class__)
print(bob.__class__.__name__)

print(list(bob.__dict__.keys()))
print(bob.__dict__)

for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])
    
# getattr
for key in bob.__dict__:
    print(key, '=>', getattr(bob, key))
    
# A generic display tool
'''
from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def lastName(self):
        return self.name.split()[-1]
        
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
class Manager(Person):
    """
    A customized Person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
        # Job name is implied
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print('---------')
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)


