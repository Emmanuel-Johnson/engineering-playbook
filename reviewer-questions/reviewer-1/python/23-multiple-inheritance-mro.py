class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")
        super().show()


class C(A):
    def show(self):
        print("Class C")
        super().show()


class D(B, C):   # Multiple Inheritance
    def show(self):
        print("Class D")
        super().show()


obj = D()
obj.show()

print(D.mro())