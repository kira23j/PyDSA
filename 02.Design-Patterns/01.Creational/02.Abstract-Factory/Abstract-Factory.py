class Dog:
    def __init__(self,name):
        self._name=name
    def speak(self):
        return "Woof"
    
class Cat:
    def __init__(self,name):
        self._name=name
    def speak(self):
        return "Meaw"
class Lion:
    def __init__(self,name):
        self._name=name
    def speak(self):
        return "Roar"
def get_pet(pet="animal"):
    """A Factory Method"""
    pets=dict(dog=Dog("Hope"),cat=Cat("Peace"),lion=Lion("strength"))
    return pets[pet]

d=get_pet("dog")
c=get_pet("cat")
l=get_pet("lion")

print(d.speak())
print(c.speak())
print(l.speak())
    