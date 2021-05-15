# Class_Coding Details
class SharedData:
    spam = 42 #Generates a class data attribute
    
x = SharedData()
y = SharedData()
x.spam = 90
print(x.spam, y.spam)

# example of this behavior that stores the same name in
# two places. Suppose we run the following class:


class MixedNames:
    data = 'spam'
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data, MixedNames.data)
        
mi = MixedNames('hp')
print(mi.display())

# Methods
class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)
        
x = NextClass()
x.printer('instance call')
x.message

# Direct class call
NextClass.printer(x, 'class call')
print(x.message)

# Calling Superclass Constructors
# Inheritance
# Attribute Tree Construction
# specializing inherited methods

class Super:
    def method(self):
        print('in Super.method')
        
class Sub(Super):
    def method(self):
        print('starting sub method')
        Super.method(self)
        print('ending Sub.method')

x = Super()
x.method()

x = Sub()
x.method()

# Class Interface Techniques

class Super1:
    def method(self):# Default behavior
        print('in Super.method')
    def delegate(self):# Expected to be defined
        self.action()
        
    def action(self):
        print('its not in mark lutz')
        
class Sub1(Super1):
    def action(self): print('spam')

class Inheritor(Super1):
    def action(self):
        print('its not in mark lutz')

class Replacer(Super1):
    def method(self): #Replace method completely
        print('in Replacer.method')
        
class Extender(Super1):#Extend method behaviour
    def method(self):
        print('starting Extender.method')
        
        Super.method(self)
        
        print('Ending Extender.method')
        
class Provider(Super1):
    def action(self): #Fill a required method
        print('In provider.action')
    
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider..')
    x = Provider()
    x.delegate()
    x = Super1()
    x.action()
    x = Sub1()
    x.delegate()
    
# Abstract Superclasses
# Attribute Names: Object Namespaces
# The “Zen” of Namespaces: Assignments Classify Names

X = 11 # Global (module) name/attribute (X, or manynames.X)
def f():
    return X # Access global X (11)
def g():
    X = 22 # Local (function) variable (X, hides module X)
    return X
class C:
    X = 33 # Class attribute (C.X)
    def m(self):
        X = 44 # Local variable in method (X)
        self.X = 55 # Instance attribute (instance.X)

print(X)
print(f())
print(g())

obj = C()
print(obj.X)

obj.m()
print(obj.X)
print(C.X)

# Nested Classes: The LEGB Scopes Rule Revisited
X = 1
def nester():
    X = 2
    print(X)
class D:
    print(X)
    def method1(self):
        print(X)
    def method2(self):
        X = 3
        print(X)
I = D()
I.method1()
I.method2()

nester()

# Namespace Dictionaries: Review
class Super2:
    def hello(self):
        self.data1 = 'spam'
        return self.data1
class Sub2(Super2):
    def hola(self):
        self.data2 = 'eggs'

a = Sub2()
print(a.__dict__)
print(a.__class__)
print(Sub2.__bases__)
print(Super.__bases__)

Y = Sub2()
print(a.hello())
print(a.__dict__)

a.hola()
print(a.__dict__)

print(list(Sub2.__dict__.keys()))
print(list(Super2.__dict__.keys()))

print(Y.__dict__)

a.data1 = 'kuttu'
# print(a.__dict__)
a.data2 = 'Puma'
print(a.__dict__)

a = Super2()
a.hello()
print(a.__dict__)

print(dir(a))

# Namespace Links: A Tree Climber
