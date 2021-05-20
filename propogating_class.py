# Propogating class type
class Commuter5:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        if isinstance(other, Commuter5):
            other = other.val
        return Commuter5(self.val + other)
        
    def __radd__(self, other):
        return Commuter5(other + self.val)
    def __str__(self):
        return '<Commuter5: %s>' % self.val
        
x = Commuter5(100)
y = Commuter5(99)
print(x+10)
print(10+y)

z = x + y
print(z)

print(z +10)
print(isinstance(z, Commuter5))
print(z + z + 1)

# The __iadd__ method
class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):
        self.val += other
        return Number(self.val)
        
x = Number(5)
x+=1
x+=1
print(x.val)

y = Number([1])
y += [2]
y += [3]
print(y.val)