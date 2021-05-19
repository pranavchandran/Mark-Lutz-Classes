# btc_am = 3678569
# purch = 1000

# Membership: __contains__, __iter__, and __getitem__
# contains.py

class Iters:
    def __init__(self, value):
        self.data = value
        
    def __getitem__(self, i):
        print('get[%s:' %i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter=> ', end='')
        self.ix = 0
        return self
        
    def __next__(self):
        print('next', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix+=1
        print(item)
        return item
        
    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data
        
    next = __next__
    
if __name__ == '__main__':
    X = Iters([10,2,3,4,5])
    print(3 in X)    
    for i in X:
        print(i, end=' | ')
        
    print()
    print([i**2 for i in X])
    print(list(map(bin, X)))
    I = iter(X)
    
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break


# for x in range(1, 10):        
#     print('#', end='')
#     print(x)

# Same thing shaved 6 lines
class Iters1:
    def __init__(self, value):
        self.data = value
        
    def __getitem__(self, i):
        print('get[%s]' %i, end='')
        return self.data[i]
        
    def __iter__(self):
        print('iter=> next', end='')
        for x in self.data:
            yield x
            print('next:', end='')
            
    def __contains__(self, x):
        print('contains: ', end= '')
        return x in self.data
        
if __name__ == '__main__':
    X = Iters1([10,2,3,4,5])
    print(3 in X)    
    for i in X:
        print(i, end=' | ')
        
    print()
    print([i**2 for i in X])
    print(list(map(bin, X)))
    I = iter(X)
    
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break

# contains only in python2
# from contains import Iters
# X = Iters('spam')
# print(X[0])

print('spam'[1:])
print('spam'[slice(1, None)])
print(X[1:])
print(X[:-1])
print(X)
print(list(X))

# Attribute Access: __getattr__ and __setattr__

