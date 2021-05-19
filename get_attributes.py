# Get attributes examples

class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age': return 40
        else: raise AttributeError(attrname)
        
X = Empty()
print(X.age)
# X.name
print(X.__dict__)
print(Empty.__dict__)

# Attribute Assignment and Deletion
# setattr

class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr, value + ' not allowed')
            
x = Accesscontrol()
# Look age is an attribute
x.age = 40
print(x.age)
print(x.__dict__)
# print(vars(x))
# x.name = 'Bob'
# self.__dict__[attr] = value + 10
# object.__setattr__(self, attr, value + 10)
# OK: doesn't loop
# OK: doesn't loop (new-style only)
x.__setattr__('age', 100)
print(x.__dict__)

# Other Attribute Management Tools
# filename: private0.py

class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value
            
class Test1(Privacy):
    privates = ['age']
    
class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'
        
if __name__ == '__main__':
    x = Test1()
    y = Test2()
    print('*'*20)
    x.name = 'Bob'
    
    print(x.name)
    # x.age = 30 it will exec of our settattr
    
    print(y.name)
    y.sex = 'male'
    print(y.sex)
    print(y.__dict__)
    # y.pay = 2000 setattr works
    



# String Representation: __repr__ and __str__
class Adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        self.data += other
z = Adder()
print(z)
class Adderrepr(Adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data

# class Adderrepr(Adder):
#     def __str__(self):
#         return '[Value: %s]' % self.data

# repr will change __str__ and __repr__ all namespace
        
o = Adderrepr(2)
o + 1
print(o)
print(repr(o), str(o))

# assert(str(o)==repr(o))
class Both(Adder):
    def __str__(self):
        return 'Value: %s' % self.data
    def __repr__(self):
        return 'addboth(%s)' %self.data

l = Both(5)

print(l)
print(str(l), repr(l))
