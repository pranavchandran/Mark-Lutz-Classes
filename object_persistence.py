# Pickes and shelves
# makedb.py
# store Person objects on a shelve database
from morerealistic import Person,Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

print(type(db), db.__dict__)

# Exploring shelves interactively
import glob
print(glob.glob('Person*'))

db = shelve.open('persondb')
print(len(db))
print(list(db.keys()))

bob = db['Bob Smith']
print(bob)
print(bob.lastName())

for key in db:
    print(key, '=>', db[key])
    
# Updating objects on a shelve
sue = db['Sue Jones']
sue.giveRaise(.20)
db['Sue Jones'] = sue
db.close()

db = shelve.open('persondb')
for key in db:
    print(key, '=>', db[key])
db.close()

db = shelve.open('persondb')
rec = db['Sue Jones']
print(rec)
print(rec.lastName())
print(rec.pay)