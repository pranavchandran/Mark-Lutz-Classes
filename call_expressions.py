# Call Expressions: __call__
class Callee:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)
        
c = Callee()
# c(1,2,3)
c(1,2,3, x=4,y=5)

class Prod:
    def __init__(self, val): self.val = val
    def __call__(self, other): return self.val * other
    
p = Prod(10)
print(p(20))
print(p(4))

# Function Interfaces and Callback-Based Code
x = lambda x: "Yes" if x%2==0 else "No"

print(x(13))
print(2)

# Function Interfaces and Callback-Based Code
class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('turn', self.color)
        
cb_b = Callback('blue')
cb_g = Callback('green')
cb_b()
cb_g()

def callback(color):
    def oncall():
        print('turn', color)
    return oncall
    
cb = callback('yellow')
cb()

cb4 = (lambda color='red': 'turn' + color)
print(cb4())

class Callback1:
    def __init__(self, color):
        self.color = color
    def changeColor(self):
        print('turn', self.color)

class Button:
    def __init__(self, command):
        self.command = command
        if self.command.__class__.__name__ == "method":
            self.command()
        pass

cb1 = Callback1("blue")
cb2 = Callback1("orange")
B1 = Button(command=cb1.changeColor)

cb3 = Callback1('blue is sky')
obj = cb3.changeColor
obj()

# Comparisons: __lt__, __gt__, and Others


