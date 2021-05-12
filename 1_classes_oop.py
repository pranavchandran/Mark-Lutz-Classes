class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)
        
class SecondClass(FirstClass):
    print('secondclass')
    def display(self):
        print(f'Current value = {self.data}')
        
# fc = FirstClass()
# fc.setdata('ram')
# fc = SecondClass()
# fc.setdata('ram')
# fc.display()

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' %self.data
    def mul(self, other):
        self.data *= other
        
a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()
print(b)

a.mul(3)
print(a)
'''
class rec: pass
rec.name = 'Bob'
rec.age = 40
print(rec.name)

x = rec()
y = rec()

print(x.name, y.name)
x.name = 'SUe'
print(rec.name, x.name, y.name)
print(list(rec.__dict__.keys()))
print(list((name for name in rec.__dict__.keys() if not name.startswith('__'))))
print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))
print(rec.__bases__)

def uppername(obj):
    print(obj.name.upper())
    return obj.name.upper()
uppername(x)

# Now it's a class method
rec.method = uppername
x.method()
y.method()
rec.method(x)
'''
rec = ('Bob', 40.5, ['dev', 'mgr'])
print(rec[0])

rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['jobs'] = ['dev', 'mgr']

print(rec['name'])

class rex: pass
rex.name = 'Bob'
rex.age = 40.5
rex.jobs = ['dev', 'mgr']
print(rex.name)

pers1 = rex()
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rex()
pers2.name = 'Sue'
pers1.jobs = ['dev', 'mgr']
pers2.age = 40.5

class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age
    def intro(self):
        return (self.name, self.jobs)
        
rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.jobs, rec2.intro())
