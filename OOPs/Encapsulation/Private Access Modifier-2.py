class Test:

    varPublic = 65
    _varProtected = 50
    __varPrivate = 25

    def pub_Method(self):
        print("Public Method")

    def _protectedMethod(self):
        print("Protected Method")

    def __PrivateMethod(self):
        print("Private Method")


class Subclass(Test):
    pass

# Deriver Code
obj = Subclass()
print(obj.varPublic)
print(obj._varProtected)
print(obj.__varPrivate)      #AttributeError: 'Subclass' object has no attribute '__varPrivate'

# Output

'''
65
50
Traceback (most recent call last):
  File "/home/ayush/Private Access Modifier-2.py", line 24, in <module>
    print(obj._varPrivate)
AttributeError: 'Subclass' object has no attribute '__varPrivate'
'''
