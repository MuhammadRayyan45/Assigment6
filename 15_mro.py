
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
print(d.show())

