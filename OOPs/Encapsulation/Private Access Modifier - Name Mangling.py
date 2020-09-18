# Private Access Modifier - Name Mangling

class Test:

    varPublic = 65
    _varProtected = 50
    __varPrivate = 25

    def pub_Method(self):
        print("Public Method")

    def _protectedMethod(self):
        print("Protected Method")

    def __PrivateMethod(self):
        return "Private Method"


class SubClass(Test):
    pass

# Deriver Code
obj = SubClass()
print(obj.varPublic)
print(obj._varProtected)
print(obj._Test__varPrivate)
print(obj._Test__PrivateMethod())
