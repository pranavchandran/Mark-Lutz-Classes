# Operator overloading
# Constructors and Expressions: __init__ and __sub__

# class Number:
#     def __init__(self, start):
#         self.data = start
#     def __sub__(self, other):
#         return Number(self.data - other)
        
# X = Number(5)
# Y = X - 2
# # print(Y.data)

# # Common Operator Overloading Methods
# # Indexing and Slicing: __getitem__ and __setitem__
# class Indexer:
#     def __getitem__(self, index):
#         return index ** 2
        
# X = Indexer()
# print(X[2])

# for i in range(5):
#     print(X[i], end=',')
    
# class Indexer1:
#     data = [5, 6, 7, 8, 9]
#     def __getitem__(self, index):
#         print('getitem:', index)
#         return self.data[index]
        
# X = Indexer1()
# print(X[0])

# class Indexer2:
#     def __getitem__(self, index):
#         if isinstance(index, int):
#             # Test usage mode
#             print('indexing', index)
#         else:
#             print('slicing', index.start, index.stop, index.step)
        
# X = Indexer2()
# X[99]
# X[1:99:2]
# X[1:]

# # Index Iteration: __getitem__
# class StepperIndex:
#     def __getitem__(self, i):
#         return self.data[i]
        
# o = StepperIndex()
# o.data = "spam"
# print(o[1])
# for item in o:
#     print(item, end=' ')

# # print(list(map(str.upper, o)))
# # (a,b,c,d) = o
# # print(a, c)

# # print(list(o), tuple(o), ''.join(o))

# # Iterable Objects: __iter__ and __next__
# # User-Defined Iterables
# class Squares:
#     def __init__(self, start, stop):
#         self.value = start - 1
#         self.stop = stop
        
#     def __iter__(self):
#         return self
        
#     def __next__(self):
#         if self.value == self.stop:
#             raise StopIteration
#         self.value += 1
#         return self.value ** 2
        
# # for i in Squares(1, 5):
# #     print(i, end=' ')
    
# # Manual Iteration
# Z = Squares(1,5)
# I = iter(Z)

# while True:
#     try:
#         print(next(I))
#     except StopIteration:
#         print('Finished')
#         break
#     except Exception as e:
#          print(e) # or whatever kind of logging you want
         
# # Single versus multiple scans
# X = Squares(1,5)
# print([n for n in X])

# print([n for n in X]) #look now exhausted

# a = [1]
# a1 = iter(a)
# b = next(a1)
# print(b)

# # print(a1)
# print(36 in Squares(1, 10))
# a,b,c = Squares(1,3)
# print(a,b,c)
# print(':'.join(map(str, Squares(1,3))))

# # # Iterator exhausted in second tuple()
# a = Squares(1,5)
# print(tuple(a))
# print(tuple(a))

# a = [1,2,3,4]
# print(tuple(a))

# li = list(Squares(1,5))
# print(tuple(li), tuple(li))

# # Classes versus generators

# def gensquares(start, stop):
#     for i in range(start, stop + 1):
#         yield i ** 2
        
# for i in gensquares(1, 5):
#     print(i,',', end=' ',)
    
# for i in (x **2 for x in range(1,6)):
#     print(i)
    
# a1 = Squares(1,10)
# print(list(a1))
# Multiple Iterators on One Object

# Multiple Iterators on One Object
# A good look to understand the loop working
# S = 'ace'
# for x in S:
#     for y in S:
#         print(x + y, end=' ')
# aa ac ae ca cc ce ea ec ee Answer

# File skipper.py
class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)
        
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item
            
if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))
    
    # for x in skipper:
    #     for y in skipper:
    #         print(x+y, end='')
            
# Coding Alternative: __iter__ plus yield
def gen(x):
    for i in range(x): yield i
    
G = gen(5)
print(G.__iter__()==G)

# print(next(G))
# print(next(G))

I = iter(G)
print(next(I), next(I))

print(list(gen(5)))
print(list(G))
    
class Squares:
    # __iter__ + yield generator
    def __init__(self, start, stop):
    # __next__ is automatic/implied
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value
            
    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
        
# s = Squares(1,10)
# print(list(s))

for i in Squares(1,5).gen(): print(i)

S = Squares(1,5)
I = iter(S)
print(next(I), next(I))

N = Squares(1,10)
print(list(N.gen()))

# Multiple iterators with yield
S = Squares(1,3).gen()
for i in S:
    for j in S:
        print('%s : %s' %(i, j))
        
#File squares_nonyield.py
class SquaresA:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        return SquaresIterA(self.start, self.stop)
        
class SquaresIterA:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    # iterator making 
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
        
b = SquaresIterA(1, 10)
print(next(b), next(b))    

# Skipper_yield.py
# Another __iter__ + yield generator
# Instance scope retained normally
# Local scope state saved auto

class SkipObjectA:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item
            
a1 = SkipObjectA([1,2,3,4])
print(list(a1))

    
            
