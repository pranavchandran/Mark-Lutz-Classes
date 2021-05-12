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
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1+percent))
        
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())
    # Use the new methods
    sue.giveRaise(.10)
    # instead of hardcoding
    print(sue.pay)
    






