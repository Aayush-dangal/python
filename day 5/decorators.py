# def star(func):
#     def wrapper():
#        print("*"*3) 
#        func()
#        print("*"*3)
#     return wrapper


# def hello():  
#     print('hello')   


# @star
# def world():   
#     print('world')   
# star (hello)()

# task
# ######################
# **********************
# world
# ######################
# **********************

def star(func):
    def wrapper():
        print("#########################")
        print("*************************")
        func()
        print("#########################")
        print("*************************")
    return wrapper

@star
def hello():
    print("Hello")

hello()

