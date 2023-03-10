class encap:
    _a=10
    c=20
    def encapfunc(self):
        _b=100
        print("accessing")
        print(self._a+2)
obj=encap()
print(obj._a)
obj.encapfunc()
print(obj.c)
