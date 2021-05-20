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