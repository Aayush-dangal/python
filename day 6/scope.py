# a=10

# def number():
#     global a
#     a=11
#     print(a)
    
# number()
# print(a)


# a=10
# def outer():
#     a=11
#     def inner():
#         a=12
#         print("inner seees a as",a)
#     inner()
#     print("outer sees a as",a)
# outer()   
# print('main aees a as',a)



# a=[1,2,3]
# print(a)

# a.append(12)
# print()



# islogin=false
# list append()
# user register and login
#{
    
#}
#using list of dictonary
# 'username':test
# 'password':123

# logout
user_list = []
def register(username, password):    
    for user in user_list:
        if user['username'] == username:
            print("Username already taken. Please choose a different one.")
            return False

    user_list.append({'username': username, 'password': password, 'islogin': False})
    print("Registration successful.")
    return True

def login(username, password):
    for user in user_list:
        if user['username'] == username and user['password'] == password:          
            user['islogin'] = True
            print("Login successful.")
            return True
    
    print("Incorrect username or password. Please try again.")
    return False

def logout(username):
    for user in user_list:
        if user['username'] == username and user['islogin']:           
            user['islogin'] = False
            print("Logout successful.")
            return True
    
    print("User not logged in.")
    return False

while True:
    print("1. Register\n2. Login\n3. Logout\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register(username, password)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(username, password)
    elif choice == '3':
        username = input("Enter your username: ")
        logout(username)
        print("Exiting program.")
    elif choice == '4':
        break
    else:
        print("Invalid user. Please try again.")

