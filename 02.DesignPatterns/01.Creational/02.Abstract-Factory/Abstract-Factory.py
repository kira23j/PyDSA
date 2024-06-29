class Dog: 
    def speak(self):
        return "dog_sound"
    def __str__(self) -> str:
        return "Dog"
    
class DogFactory:
    """this is concrete factory """
    def get_pet(self):
        """return dog object"""
        return Dog()
    
    def get_food(self):
        """returns a dog food object"""
        return "dog_food"
        
class Petstore:
    """pet factory is our abstract factory"""
    def __init__(self,pet_factory=None) :
        self._pet_factory=pet_factory
    
    def show_pet(self):
        pet=self._pet_factory.get_pet()
        pet_food=self._pet_factory.get_food()
        print("our pet is '{}' ".format(pet))
        print("our pet says hello by '{}' ".format(pet.speak()))
        print("its food is '{}' ".format(pet_food))
        
# create a concrete factory  
factory=DogFactory()
# create a pet store housing for abstract factory
shop=Petstore(factory)

# create a pet store housing our abstract factory
shop.show_pet()