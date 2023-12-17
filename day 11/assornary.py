class person:
    def __init__(self,name,age,password) -> None:
        self.name=name
        self._age=age
        self.__password=password
    @property   
    def get_password(self):
        return self.___password
    
    def set_password(self,password):
        self.___password=password
        
        
    # password=property(get_password.set_password)
        
person=person('ram',12,'Aayush')
print(person.name)
print(person._age)
# person.set_password('123')
# print(person.get_password())
person.password=123
print(person.password)