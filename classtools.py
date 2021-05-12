# Assorted class utilities and tools

class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s'%(key, getattr(self, key)))
        return ', '.join(attrs)
        
    def __repr__(self):
        return '[%s: %s]'%(self.__class__.__name__, self.gatherAttrs())
        
class TopTest(AttrDisplay):
    count = 0
    def __init__(self):
        self.attr1 = TopTest.count
        self.attr2 = TopTest.count+1
        TopTest.count += 2
        
    def gatherAttrs(self):
        return 'Spam'
        
class SubTest(TopTest): pass
x, y = TopTest(), SubTest()
print(x)
print(y)

# Instance vs Class Attributes
# Name Considerations in Tool Classes
# Our Classes Final Form
# Step7(Final): Storing objects in a Database

