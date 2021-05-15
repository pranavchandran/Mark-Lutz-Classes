# Operator overloading
# Constructors and Expressions: __init__ and __sub__

class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)
        
X = Number(5)
Y = X - 2
# print(Y.data)

# Common Operator Overloading Methods
# Indexing and Slicing: __getitem__ and __setitem__
class Indexer:
    def __getitem__(self, index):
        return index ** 2
        
X = Indexer()
print(X[2])

for i in range(5):
    print(X[i], end=',')
    
class Indexer1:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]
        
X = Indexer1()
print(X[0])

class Indexer2:
    def __getitem__(self, index):
        if isinstance(index, int):
            # Test usage mode
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)
        
X = Indexer2()
X[99]
X[1:99:2]
X[1:]