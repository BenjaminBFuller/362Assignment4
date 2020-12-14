# Benjamin Fuller Test Singleton Program
# Creates Instances of Single elements to returns

class Simpleton(object):
    class __Simpleton:
        def __init__(self):
            self.val = None

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __new__(cls):
        if not Simpleton.instance:
            Simpleton.instance = Simpleton.__Simpleton()
        return Simpleton.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


x = Simpleton()
x.val = 'Burger'
print(x)
y = Simpleton()
y.val = 'Fries'
print(y)
z = Simpleton()
z.val = 'Drink'
print(z)
print(x)
print(y)
