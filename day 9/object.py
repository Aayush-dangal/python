class house:    
    def __init__(self,name,window,door,color,price=1000):
        self.price=price
        self.name=name
        self.window=window
        self.door=door
        self.color=color
            
    def __str__(self) -> str:
        return f"{self.name} ko ghar"
    
    def __eq__(self, value: object) -> bool:
        return self.window==value.window
    
    def set_color(self,color):
        self.color=color
        
    def get_color(self):
        return self.color    
            
ram_ko_ghar=house(name="ram")
print(ram_ko_ghar)
shyam_ko_ghar=house(name="shyam",color="black")

is_name=ram_ko_ghar.__eq__(shyam_ko_ghar)
print(is_name)



# ram_ko_ghar.set_color=("blue")
# print(ram_ko_ghar.get_color())
# print(ram_ko_ghar.door)
# print(ram_ko_ghar.window)