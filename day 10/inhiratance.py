# class grandfather(object):
#     def __init__(self) -> None:
#         print("grandfather")
        
#     def get_house(self):
#         return self.house
        
    
#     house="luxery"
    
# class grandmother:
#     def __init__(self) -> None:
#         print("grandmother")
#     jewallary="gold"  
    
# class father(grandfather,grandmother):
#     # def __init__(self) -> None:
#     #     print("father")
#     car="marcedes"
#     def get_house(self):
#         print(super().get_house())
#         return"ghar"
    
# class son(father):
#     console="ps5"
    
# grandfather=grandfather()
# print(grandfather.house)    
# father=father()
# print(father.car)
# father=father()
# print("get_house")
# print(son.console)

# print(isinstance(son,object))


#task
# example of inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

animal_instance = Animal("Generic Animal")
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")


animal_instance.speak()  
dog_instance.speak()    
cat_instance.speak()    
